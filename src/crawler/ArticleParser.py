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
    done = 0
    ignoreline = -1
    gottext = 0
    html = ""
    firstonly = [0,0,0,0,0,0,0]

    def __init__(self):
        '''
        Constructor
        '''
        HTMLParser.__init__(self)
        self.mech = mechanize.Browser()
        
    '''
    removes script tags from html so htmlparser doesn't break
    '''
    @staticmethod
    def pre_parse(html, tag):
        counter = 1
        start = html.find("<" + tag)
        while (start != -1 and counter < 100):
#            print counter
            counter += 1
            start = html.find("<" + tag)
            if start != -1:
                end = html.find("</" + tag + ">")
                firsthalf = html[:start]
                secondhalf = html[end + len("<\\" + tag + ">"):]
#                print html[start:end]
                html = firsthalf + secondhalf
                if end ==  -1:
                    start = -1
        return html

    def get_HTML(self, url):
        self.mech.open(url)
        response = self.mech.response()
        self.html = response.read()
        return self.html

    def get_tag_by_name(self, tag, attrs, isfound):
        found_description = 0
        if (self.firstonly[isfound] == 0):
            for attr in attrs:
                if attr[1].find(tag) != -1:
                    found_description = 1
                    print attr[1]
                if attr[0].find("content") != -1 and found_description == 1:
                    print attr[1]
                    self.firstonly[isfound] = 1
    
    def handle_starttag(self, tag, attrs):
        if self.ignoreline < self.getpos()[0]:
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
                self.gottext = 1
   
    def handle_data(self,data):
#        if self.gottext:
#            print data
        self.gottext = 0

    def handle_endtag(self, tag):
        if tag == "html":
            self.done = 1
            print "done"
                
    def delete_line(self, data, pos):
        print "deleted line" + str(pos[0])
        res = data.split("\n")
        print "res lines" + str(len(res))
        res.pop(pos[0]-1)
        self.ignoreline = pos[0]
        return "\n".join(res)
    
    def skip_broken_line(self):
        temphtml = self.html
        pos = self.getpos()
        self.reset()
        self.html = self.delete_line(temphtml, pos)
        
#parser = ArticleParser()

#parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
#html = parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
##html = parser.get_HTML("http://www.aljazeera.com/news/asia-pacific/2012/04/201242733733409278.html")
##while (parser.done == 0):
##    try:
#print "running"
#html = ArticleParser.pre_parse(html, "script")
#print "finished"
#parser.feed(html)
#    except:
#        print "Unexpected error:", sys.exc_info()
#        parser.skip_broken_line()
