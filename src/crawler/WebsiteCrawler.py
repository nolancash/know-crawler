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
        for link in self.mech.links(url_regex=url):
            link.url
            print link.url

            
        
        
     


crawler = WebsiteCrawler()
print crawler.get_links("http://www.nytimes.com/")
