"""
Created on Apr 23, 2012

@author: Nolan, Tyler
"""

import urllib2
from HTMLParser import HTMLParser
import mechanize
import Utilities

"""
Article Parser extends the HTMLParser class and is used to parse a news article page for a summary of its meta information
and then returns a list of strings that represents that summary in this format
["title", "description", "keywords", "author", "date", "url"].
"""
class ArticleParser(HTMLParser):
    def __init__(self):
        """
        Constructor for the Article parser
        """
        HTMLParser.__init__(self)
        self.__ignore_line = -1
        self.__got_text = False
        self.__got_title = False
        self.__title = ""
        self.__html = ""
        self.__text = []
        self.__util = Utilities.Utilities()
        self.mech = mechanize.Browser()
        self.results = ["null", "null", "null", "null", "null", "null", "null"]
        
    """
    Removes script tags from __html so ArticleParser doesn't break on malformed html tags in embedded javascript.
    """
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

    """
    Takes a url and returns the html as a string from the passed url.
    """
    def get_html(self, url):
        try:
            self.mech.open(url)
            response = self.mech.response()
            self.__html = response.read()
        except urllib2.URLError:
            print "Url not valid."
            pass
        except mechanize._mechanize.BrowserStateError:
            print "Empty url string."
            pass
        return self.__html
    
    """
    Parses the passed attributes list of tuples attrs for the given tag and saves the value of the tag into the results array
    for this object at the passed result_index. If one already has been found for this tag it is not added.
    """
    def __get_tag_by_name(self, tag, attrs, result_index):
        found_description = False
        content = None
        if (self.results[result_index] == "null"):
            for attr in attrs:
                if (attr[1] != None and attr[1].lower().find(tag) != -1):
                    found_description = True
#                    print attr[1]
                if attr[0].find("content") != -1:
                    content = attr[1].decode("utf-8").encode("ascii", "ignore")
            try:
                if content != None and found_description:
                    self.results[result_index] = content
            except UnicodeDecodeError:
                print "Decode error: Article attribute."
                pass
    
    """
    Overides the HTMLparser handle_starttag and takes a string tag which represents the html tag that has been found and
    the list of tuples attrs that are the tags attributes and parses them if they are a meta tag.
    """
    def handle_starttag(self, tag, attrs):
        if self.__ignore_line < self.getpos()[0]:
            if tag == "meta":
#                print "Encountered a start tag:", tag
                self.__get_tag_by_name("title", attrs, 0)
                self.__get_tag_by_name("description", attrs, 1)
                self.__get_tag_by_name("keywords", attrs, 2)
                self.__get_tag_by_name("author", attrs, 3)
                self.__get_tag_by_name("og:type", attrs, 4)
            elif tag == "p":
                self.__got_text = True
            elif tag == "title":
                self.__got_title = True
    
    """
    This function gets called when an html tag has text inside of it. If the start tag was a p tag then it is processed.
    If the title attribute has not been set, then we set the title with the title tag.
    """
    def handle_data(self,data):
#        TODO: process p tags
        if self.__got_text:
            self.__text.append(data)
        
        elif self.__got_title:
            try:
                self.__title += data.decode("utf-8").encode("ascii", "ignore")
            except UnicodeDecodeError:
                print "Decode error: Title."
                pass
            
    """
    This function gets called to signal the closing of a paragraph tag or the end of
    the html.
    """
    def handle_endtag(self, tag):
        if tag == "p":
            self.__got_text = False
        if tag == "html":
            if self.results[2] == "null":
                self.results[2] = ", ".join(self.__get_top_words())
            else:
                self.results[2] += ", " + ", ".join(self.__get_top_words())
            self.results[2] = self.results[2].lower()
            locations = self.__get_related_locations()
            if len(locations) > 0:
                self.results[5] = locations.pop()
            if len(locations) > 0:
                self.results[6] = ", ".join(locations)
        if tag == "title":
            self.__got_title = False
            self.results[0] = self.__title.strip()
#            print self.results[2]
    
    """
    Helper function to get the top 10 uncommon words in the text.
    """
    def __get_top_words(self):
        common_words = self.__util.common_words
        word_counts = self.__util.word_frequencies(", ".join(self.__text))
        top_10_words = self.__util.top_k_words(word_counts, 10, common_words)
        return top_10_words
    
    """
    Helper function to get the top 4 locations in the text.
    """
    def __get_related_locations(self):
        common_locations = self.__util.common_locations
        locations = self.__util.get_locations(", ".join(self.__text), common_locations)
        top_4_locations = self.__util.top_k_locations(locations, 4)
        return top_4_locations