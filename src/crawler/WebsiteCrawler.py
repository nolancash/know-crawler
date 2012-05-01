'''
Created on Apr 23, 2012

@author: Nolan
'''
import sys
import os, re
import urlparse
import time
import MySQLdb
from ArticleParser import ArticleParser
from urllib2 import HTTPError
import mechanize


class WebsiteCrawler(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.mech = mechanize.Browser()
        
    def get_links(self,base_url):
        try:
            print "opening"
            self.mech.open(base_url)
#            response = self.mech.response()
            print "loaded response"
    #        print response.info()
    #        print response.read()
            links = self.mech.links(url_regex=base_url)
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
            pass
            
            
    def __normalize_url(self, url):
        res = ""
        if url.find("?") != -1:
            res = url[0:url.find("?")]
        if res.find("#") != -1:
            res = res[0:res.find("#")]
        return res

    def parse_articles(self, articles):
        for article in articles:
            print "running"
            print article
            parser = ArticleParser()
            try:
                html = parser.get_html(article)
                if len(html) > 10:
                    print "full"
                html = ArticleParser.pre_parse(html, "script")
#                time.sleep(1)
                print "finished"
                try:
                    parser.feed(html)
                except UnicodeDecodeError:
                    print "Bad character."
                del parser
                del html
            except HTTPError:
                pass
            

crawler = WebsiteCrawler()
#print crawler.get_links("http://www.nytimes.com/reuters/2012/04/30/sports/golf/30reuters-golf-european.html")
#try:
#    print crawler.get_links("http://www.nytimes.com/reuters/2012/04/30/sports/golf/30reuters-golf-european.html")
#except Exception, e:
#    print e
#for article in crawler.get_links("http://www.washingtonpost.com/politics/"):
#    print article
crawler.parse_articles(crawler.get_links("http://www.nytimes.com/"))

