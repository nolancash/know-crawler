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
#        self.__done = 0
        self.__ignore_line = -1
        self.__got_text = False
        self.__html = ""
        self.__text = []
        self.mech = mechanize.Browser()
        self.results = ["null", "null", "null", "null", "null", "null"]
        
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
        if (self.results[result_index] == "null"):
            for attr in attrs:
                if attr[0] != "content" and (attr[1] != None and attr[1].find(tag) != -1):
                    found_description = True
#                    print attr[1]
                if attr[0].find("content") != -1 and found_description:
                    try:
                        self.results[result_index] = attr[1].decode("utf-8").encode("ascii", "ignore")
                    except UnicodeDecodeError:
                        print "Decode error."
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
                self.__get_tag_by_name("date", attrs, 4)
                self.__get_tag_by_name("type", attrs, 5)
            if tag == "p":
                self.__got_text = True
    
    """
    This function gets called when an html tag has text inside of it. If the start tag was a p tag then it is processed.
    """
    def handle_data(self,data):
#        TODO: process p tags
        if self.__got_text:
            self.__text.append(data)
            pass
        
    """
    This function gets called to signal the closing of a paragraph tag or the end of
    the html.
    """
    def handle_endtag(self, tag):
        if tag == "p":
            self.__got_text = False
        if tag == "html":
            print self.__get_top_words()
    
    """
    Helper function to get the top 5 uncommon words in the text.
    """
    def __get_top_words(self):
        util = Utilities.Utilities()
        common_words = util.common_words
        word_counts = util.word_frequencies(", ".join(self.__text))
        top_5_words = util.top_k_unique_words(word_counts, 5, common_words)
        return top_5_words
            
parser = ArticleParser()
html = parser.get_html("http://www.nytimes.com/2012/05/13/business/student-loans-weighing-down-a-generation-with-heavy-debt.html")
parser.feed(html)
                
