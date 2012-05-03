'''
Created on Apr 23, 2012

@author: Nolan, Tyler
'''

from ArticleParser import ArticleParser
from urllib2 import HTTPError
import mechanize

'''
Created on Apr 23, 2012
This class oversees all of the crawling of a news website. It collects all of the links on a page that 
it thinks are news articles then it gathers all the information off of the pages that it thinks are 
news articles saves it.
'''
class WebsiteCrawler(object):

    """
    Creates a website crawler object.
    """
    def __init__(self):
        '''
        Constructor
        '''
        self.mech = mechanize.Browser()
#        self.mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.__article_results = []
    
    """
    Takes a url as a parameter and returns a list of strings that are links on a page that look like 
    links to articles.
    """    
    def get_links(self,base_url):
        try:
            print "opening"
            self.mech.open(base_url)
#            response = self.mech.response()
            print "loaded response"
    #        print response.info()
    #        print response.read()
#            links = self.mech.links(url_regex=base_url)
#            for l in self.mech.links():
#                print l
            articles = []
            for link in self.mech.links(url_regex=base_url):
    #            print link.url        
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
            
    """
    Takes a url and strips it of all url encoded parameters.
    """    
    def __normalize_url(self, url):
        res = ""
        if url.find("?") != -1:
            res = url[0:url.find("?")]
        if res.find("#") != -1:
            res = res[0:res.find("#")]
        return res

    """
    Given a list of strings that represent urls this method parses them and returns a list. This list contains summaries of 
    articles which are themselfs list with the following structure ["title", "description", "keywords", "author", "date", "url"].
    """
    def parse_articles(self, articles):
        for article in articles:
#            print "running"
#            print article
            parser = ArticleParser()
            try:
                html = parser.get_html(article)
#                if len(html) > 10:
#                    print "full"
                html = ArticleParser.pre_parse(html, "script")
#                time.sleep(1)
#                print "finished"
                try:
                    parser.feed(html)
                    result = parser.results
                    result.append(article)
                    self.__article_results.append(result)
                except UnicodeDecodeError:
                    print "Bad character."
                del parser
                del html
            except HTTPError:
                pass
#        for article in self.__article_results:
#            for tag in article:
#                print tag
#            print "====="
        for l in self.__article_results:
            print l
        return self.__article_results
