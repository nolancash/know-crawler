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
    html = ""

    def __init__(self):
        '''
        Constructor
        '''
        HTMLParser.__init__(self)
        self.mech = mechanize.Browser()
        
    def get_HTML(self, url):
        self.mech.open(url)
        response = self.mech.response()
        self.html = response.read()
        return self.html
    
    def handle_starttag(self, tag, attrs):
        if self.ignoreline < self.getpos()[0]:
            if tag == "meta" or tag == "p":
                print "Encountered a start tag:", tag
                for attr in attrs:
                    print attr
    def handle_endtag(self, tag):
        if tag == "html":
            self.done = 1
            print "done"
#    def handle_data(self, data):
#        print "Encountered some data  :", data

                
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
        
parser = ArticleParser()

#parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
html = parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
while (parser.done == 0):
    try:
        print "running"
        parser.feed(html)
    except:
        print "Unexpected error:", sys.exc_info()
        parser.skip_broken_line()
