'''
Created on Apr 23, 2012

@author: Nolan
'''
import sys
import os, re
import urlparse
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
        self.mech.open(baseurl)
        response = self.mech.response()
        #print response.info()
        #print response.read()
        links = self.mech.links(url_regex=baseurl)
        articles = []
        for link in self.mech.links(url_regex=baseurl):
#            print link.url        
            nurl = self.__normalize_url(link.url)
            if len(nurl) - nurl.rfind("/") > 20 and len(nurl) > len(baseurl):
                articles.append(nurl)
        
        for name in set(articles):
            print name
            
    def __normalize_url(self, url):
            if url.find("?") != -1:
                return url[0:url.find("?")]
            else:
                return url

        
        
     


crawler = WebsiteCrawler()
print crawler.get_links("http://www.nytimes.com")

