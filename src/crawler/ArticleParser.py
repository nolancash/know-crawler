'''
Created on Apr 23, 2012

@author: Nolan
'''

import sys
import os, re
import urlparse
from urllib2 import HTTPError
from HTMLParser import HTMLParser
import mechanize

class ArticleParser(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        HTMLParser.__init__(self)
        self.__done = 0
        self.__ignoreline = -1
        self.__gottext = 0
        self.__html = ""
        self.__firstonly = [0,0,0,0,0,0,0]
        self.mech = mechanize.Browser()
        
    '''
    removes script tags from __html so ArticleParser doesn't break
    '''
    @staticmethod
    def pre_parse(html, tag):
        start = html.find("<" + tag)
        while start != -1:
            end_tag = "</" + tag + ">"
            end = html.find(end_tag)
            first_half = html[:start]
            second_half = html[end + len(end_tag):]
#           print __html[start:end]
            html = first_half + second_half
            start = html.find("<" + tag)
        return html

    def get_HTML(self, url):
        self.mech.open(url)
        response = self.mech.response()
        self.__html = response.read()
        return self.__html

    def get_tag_by_name(self, tag, attrs, isfound):
        found_description = 0
        if (self.__firstonly[isfound] == 0):
            for attr in attrs:
                if attr[1].find(tag) != -1:
                    found_description = 1
                    print attr[1]
                if attr[0].find("content") != -1 and found_description == 1:
                    print attr[1]
                    self.__firstonly[isfound] = 1
    
    def handle_starttag(self, tag, attrs):
        if self.__ignoreline < self.getpos()[0]:
            if tag == "meta":
#                print "Encountered a start tag:", tag
                self.get_tag_by_name("title", attrs, 0)
                self.get_tag_by_name("description", attrs,1)
                self.get_tag_by_name("keywords", attrs,2)
                self.get_tag_by_name("author", attrs,3)
                self.get_tag_by_name("date", attrs,4)
                self.get_tag_by_name("time", attrs,5)  
                self.get_tag_by_name("type", attrs,5)
            if tag == "p":
                self.__gottext = 1
   
    def handle_data(self,data):
#        if self.__gottext:
#            print data
        self.__gottext = 0

    def handle_endtag(self, tag):
        if tag == "__html":
            self.__done = 1
            print "__done"
                
    def delete_line(self, data, pos):
        print "deleted line" + str(pos[0])
        res = data.split("\n")
        print "res lines" + str(len(res))
        res.pop(pos[0]-1)
        self.__ignoreline = pos[0]
        return "\n".join(res)
    
    def skip_broken_line(self):
        temphtml = self.__html
        pos = self.getpos()
        self.reset()
        self.__html = self.delete_line(temphtml, pos)
        
#parser = ArticleParser()

#parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.__html")
#__html = parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
##__html = parser.get_HTML("http://www.aljazeera.com/news/asia-pacific/2012/04/201242733733409278.__html")
#while (parser.__done == 0):
#    try:
#print "running"
#__html = ArticleParser.pre_parse(__html, "script")
#print "finished"
#parser.feed(__html)
#    except:
#        print "Unexpected error:", sys.exc_info()
#        parser.skip_broken_line()
