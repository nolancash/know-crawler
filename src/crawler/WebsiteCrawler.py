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
        
        # Cookie Jar
#        cj = cookielib.LWPCookieJar()
#        self.mech.set_cookiejar(cj)
        
        # Browser options
#        self.mech.set_handle_equiv(True)
#        self.mech.set_handle_gzip(True)
#        self.mech.set_handle_redirect(True)
#        self.mech.set_handle_referer(True)
#        self.mech.set_handle_robots(False)
        
        # Follows refresh 0 but not hangs on refresh > 0
        self.mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        
        # Want debugging messages?
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)
        
        self.mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.__article_results = []
    
    """
    Takes a url as a parameter and returns a list of strings that are links on a page that look like 
    links to articles.
    """
    @TimeoutException.timeout(45)    
    def get_links(self,base_url):
        try:
            self.mech.open(base_url)
            response = self.mech.response()
#            print self.mech.geturl()
            articles = []
            for link in self.mech.links(url_regex=base_url + "|^/"):
                normal_url = self.__normalize_url(link.url)
                if len(normal_url) - normal_url.rfind("/") > 20 and len(
                    normal_url) > len(base_url):
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
        except TimeoutException:
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
    @TimeoutException.timeout(60)
    def parse_articles(self, articles):
        try:
            if articles:
                for article in articles:
                    parser = ArticleParser()
                    try:
                        html = parser.get_html(article)
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
        except TimeoutException:
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

