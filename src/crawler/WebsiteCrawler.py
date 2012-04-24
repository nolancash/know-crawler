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
    def get_links(self,url):
        self.mech.open(url)
        response = self.mech.response()
        #print response.info()
        #print response.read()
        links = self.mech.links(url_regex=url)
        articles = []
        for link in self.mech.links(url_regex=url):
#            print link.url
            articles.append(link.url)
        for url in articles:
            print url

            
        
        
     


crawler = WebsiteCrawler()
print crawler.get_links("http://seattletimes.nwsource.com/")
