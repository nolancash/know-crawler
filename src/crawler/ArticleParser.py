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
#        self.__done = 0
        self.__ignore_line = -1
        self.__got_text = 0
        self.__html = ""
        self.__first_only = [0,0,0,0,0,0,0]
        self.mech = mechanize.Browser()
        self.results = ["","","","","","",""]
        
    '''
    removes script tags from __html so ArticleParser doesn't break
    '''
    @staticmethod
    def pre_parse(html, tag):
        start = html.find("<" + tag)
        end_tag = "</" + tag + ">"
        while start != -1:
            end = html.find(end_tag, start)
            if start < end:
                first_half = html[:start]
                second_half = html[end + len(end_tag):]
    #           print __html[start:end]
                html = first_half + second_half
                start = html.find("<" + tag)
            else:
                start = -1
        return html

    def get_html(self, url):
        self.mech.open(url)
        response = self.mech.response()
        self.__html = response.read()
        return self.__html

    def get_tag_by_name(self, tag, attrs, result_index):
        found_description = 0
        if (self.__first_only[result_index] == 0):
            for attr in attrs:
                if attr[1].find(tag) != -1:
                    found_description = 1
#                    print attr[1]
                if attr[0].find("content") != -1 and found_description == 1:
                    self.results[result_index] = attr[1]
#                    print attr[1]
                    self.__first_only[result_index] = 1
    
    def handle_starttag(self, tag, attrs):
        if self.__ignore_line < self.getpos()[0]:
            if tag == "meta":
#                print "Encountered a start tag:", tag
                self.get_tag_by_name("title", attrs, 0)
                self.get_tag_by_name("description", attrs,1)
                self.get_tag_by_name("keywords", attrs,2)
                self.get_tag_by_name("author", attrs,3)
                self.get_tag_by_name("date", attrs,4)
                self.get_tag_by_name("time", attrs,5)  
                self.get_tag_by_name("type", attrs,6)
            if tag == "p":
                self.__got_text = 1
   
    def handle_data(self,data):
#        if self.__got_text:
#            print data
        self.__got_text = 0

#    def handle_endtag(self, tag):
#        if tag == "html":
#            self.__done = 1
#            print "done"
                
        
#parser = ArticleParser()

#parser.get_html("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.__html")
#__html = parser.get_html("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
##__html = parser.get_html("http://www.aljazeera.com/news/asia-pacific/2012/04/201242733733409278.__html")
#while (parser.__done == 0):
#    try:
#print "running"
#__html = ArticleParser.pre_parse(__html, "script")
#print "finished"
#parser.feed(__html)
#    except:
#        print "Unexpected error:", sys.exc_info()
#        parser.skip_broken_line()
