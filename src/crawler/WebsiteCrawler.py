"""
Created on Apr 23, 2012

@author: Nolan, Tyler
"""
from ArticleParser import ArticleParser
from urllib2 import HTTPError
from urlparse import urljoin
import mechanize
import HTMLParser
import urllib2
import TimeoutException
import DBManager
import sys
import re
 
"""
This class oversees all of the crawling of a news website. It collects all of the links on a page that 
it thinks are news articles then it gathers all the information off of the pages that it thinks are 
news articles saves it.
"""
class WebsiteCrawler(object):

    """
    Creates a website crawler object.
    """
    def __init__(self):
        """
        Constructor
        """
        self.mech = mechanize.Browser()
        
        # Follows refresh 0 but not hangs on refresh > 0
        self.mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        
        self.mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.__article_results = []
    
    """
    Takes a url as a parameter and returns a list of strings that are links on a page that look like 
    links to articles.
    """
    @TimeoutException.timeout(45)    
    def get_links(self,base_url):
        try:
            articles = []
            self.mech.open(base_url)
#            response = self.mech.response()
#            print response.read()
#            print self.mech.geturl()
            for link in self.mech.links():
#                print link
                normal_url = self.__normalize_url(link.url)
                index = normal_url.rfind("/")
                if index == (len(normal_url) - 1):
                    index = normal_url[:index].rfind("/")
                if index != -1:
                    file_name = normal_url[index:]
#                    print "file: " + file_name
                    if (len(file_name) > 18 or len(re.sub("[^0-9]", "", file_name)) > 7) and len(
                        normal_url) > len(base_url):
    #                if len(normal_url) - normal_url.rfind("/") > 17 and len(
    #                    normal_url) > len(base_url):
#                        print normal_url
                        if normal_url.find(self.mech.geturl()) != -1:
                            articles.append(normal_url)
            articles = set(articles)
            return articles
        except HTTPError:
            print "Http error."
            pass
        except mechanize._form.ParseError:
            print "Parser error."
            pass
        except mechanize._mechanize.BrowserStateError:
            print "Empty url."
            pass
        except urllib2.URLError:
            print "Url error."
            pass
        except TimeoutException.TimeoutException:
            self.__blacklist_source(base_url, articles)
            pass
            
    """
    Takes a url and strips it of all url encoded parameters.
    """    
    def __normalize_url(self, url):
        res = url
        baseurl = self.mech.geturl()
        if url.find(baseurl) == -1 and len(baseurl) > 3:
            res = urljoin(baseurl[:len(baseurl)], url)
#            print res
        if url.find("?") != -1:
            res = url[0:url.find("?")]
        if res.find("#") != -1:
            res = res[0:res.find("#")]
#        print res
        return res

    """
    Given a list of strings that represent urls this method parses them and returns a list. This list contains summaries of 
    articles which are themselves list with the following structure ["title", "description", "keywords", "author", "date", "url"].
    """
    @TimeoutException.timeout(90)
    def parse_articles(self, articles):
        try:
            if articles:
                print "Parsing articles: " + str(len(articles))
                for article in articles:
#                    print article
                    parser = ArticleParser()
                    try:
                        html = parser.get_html(article)
                        if html:
                            html = ArticleParser.pre_parse(html, "script")
                            try:
                                parser.feed(html)
                                result = parser.results
                                result.append(article)
                                self.__article_results.append(result)
                            except UnicodeDecodeError:
                                print "Bad character."
                            except HTMLParser.HTMLParseError:
                                print "Bad html."
                            del parser
                            del html
                    except HTTPError:
                        print "HTTP error."
                        pass
                    sys.stdout.flush()
        except TimeoutException.TimeoutException:
            self.__blacklist_source(self.mech.geturl(), self.__article_results)
            pass
        finally:
            sys.stdout.flush()
            return self.__article_results
    
    """
    This function is called when there is a timeout exception and checks to see
    whether or not a source should be blacklisted.
    """    
    def __blacklist_source(self, url, results):
        print "Timeout Exception: " + str(len(results)) + " articles: " + str(url)
        if len(results) == 0 or results == None:
            db = DBManager.DBManager()
            db.blacklist(url)

#a = WebsiteCrawler()
#link = a.get_links("http://guardian.co.tt/")
#for l in link:
#    print l
#print len(link)
#q = a.parse_articles(link)
#for z in q:
#    print z