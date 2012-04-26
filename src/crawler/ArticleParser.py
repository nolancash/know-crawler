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

    def __init__(self):
        '''
        Constructor
        '''
        HTMLParser.__init__(self)
        self.mech = mechanize.Browser()
        
    def get_HTML(self, url):
        self.mech.open(url)
        response = self.mech.response()
        return response.read()
    
    def handle_starttag(selfself, tag, attrs):
        if tag == "meta":
            print "Encountered a start tag:", tag
            for attr in attrs:
                print attr
    def handle_endtag(self, tag):
        if tag == "html":
            self.done = 1
#    def handle_data(self, data):
#        print "Encountered some data  :", data

                
    def delete_line(self, input, pos):
        res = input.split("\n")
        res.pop(pos[0]-1)
        return "\n".join(res)
        
parser = ArticleParser()

#parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
html = parser.get_HTML("http://www.nytimes.com/2012/04/26/us/considering-arizona-immigration-law-justices-are-again-in-political-storm.html")
while (parser.done == 0):
    try:
        parser.feed(html)
    except:
        print "oh shit"
        html = parser.delete_line(html, parser.getpos())
        parser.reset()
        pass
