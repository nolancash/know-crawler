'''
Created on Apr 23, 2012

@author: Nolan
'''
import sys
import os, re
import urlparse
import time
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
    def get_links(self,baseurl):
        print "opening"
        self.mech.open(baseurl)
        response = self.mech.response()
        print "loaded response"
#        print response.info()
#        print response.read()
        links = self.mech.links(url_regex=baseurl)
        articles = []
        for link in self.mech.links(url_regex=baseurl):
#            print link.url        
            nurl = self.__normalize_url(link.url)
            if len(nurl) - nurl.rfind("/") > 20 and len(nurl) > len(baseurl):
                articles.append(nurl)
        articles = set(articles)
        return articles
            
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
            html = parser.get_HTML(article)
            if len(html) > 10:
                print "full"
            html = ArticleParser.pre_parse(html, "script")
            time.sleep(1)
            print "finished"
            parser.feed(html)
            del parser
            del html

crawler = WebsiteCrawler()
#print crawler.get_links("http://www.aljazeera.com/")
#for article in crawler.get_links("http://www.washingtonpost.com/politics/"):
#    print article
crawler.parse_articles(crawler.get_links("http://www.washingtonpost.com/politics/"))

