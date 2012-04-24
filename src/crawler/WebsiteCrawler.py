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
        