'''
Created on May 9, 2012

@author: Tyler, Nolan
'''

import re
import DBManager

"""
This class contains all of the utility functions required for the webcrawler.
These functions include calculating the most frequently used words in a piece
of text and generating a list of common words.
"""

class Utilities(object):
    
    """
    Constructs a Utilities object and generates a list of common words and common locations.
    """
    def __init__(self):
        self.common_words = []
        self.common_locations = []
        rows = DBManager.DBManager().send_query("select * from common_words;")
        for row in rows:
            self.common_words.append(row[0])
        rows = DBManager.DBManager().send_query("select cntry_name from world_countries;")
        for row in rows:
            self.common_locations.append(row[0])
    
    """
    Makes Utilities a singleton.
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Utilities, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    """
    Converts text input into a list of words.
    This function assume all text has already been converted to proper ASCII encoding.
    """
    def word_list(self, text, ignore_case = True):    
        # Changes all text to lowercase.
        if ignore_case:
            text = text.lower()
    
        # Removes ASCII apostrophes from the text.
        text = text.replace("'", "")
        
        # Removes commas from the text. We assume that all text
        # is formatted correctly in that there are no typographic errors.
        text = text.replace(",", "")
        
        # Replaces all non-word character with spaces to represent word boundaries.
        rx = re.compile("[^\w ]")
        text = rx.sub(" ", text)    
        
        # Splits words that are divided by spaces.
        text = text.split()
        
        # If any "empty words" have been manufactured by previous processes, drop them.
        text = [x for x in text if len(x) > 1]
        return text
    
    """
    Takes a string of text and returns list of unique words and their frequencies.
    """
    def word_frequencies(self, text):
        words = self.word_list(text)
        unique_words = set(words)
        return sorted([(words.count(word), word) for word in unique_words])
    
    """
    Takes a list of word frequencies and returns up to max_num of the most
    frequently used words that do no belong to common_words. Returns
    an empty list if max_num <= 0 or if all of the words in word_counts
    are found in common_words.
    """
    def top_k_words(self, word_counts, max_num, common_words):
        result = []
        if max_num > 0:
            count = 0
            while (count < max_num) and word_counts:
                word = word_counts.pop()[1]
                if not (word in common_words):
                    result.append(word)
                    count += 1
        return result
    
    """
    Takes a string and a list of common locations and returns a dictionary
    mapping any found locations in the text to their number of occurrences.
    """
    def get_locations(self, text, common_locations):
        results = {}
        text = text.lower()
        for word in common_locations:
            word = word.lower()
            if word in text:
                results[word] = -1
                pos = 0
                while pos < len(text) and pos != -1:
                    results[word] += 1
                    if text[pos+len(word):].find(word) != -1:
                        pos += text[pos+len(word):].find(word) + len(word)
                    else:
                        pos = -1
        return results
    
    """
    Takes a dictionary of locations and frequencies and returns up to 
    max_num of the most frequently used locations. Returns
    an empty list if max_num <= 0.
    """
    def top_k_locations(self, locations_dict, max_num):
        result = []
        if max_num > 0:
            count = 0
            sorted_locs = sorted(locations_dict.iteritems(), key=lambda (k,v): (v,k))
            while (count < max_num) and sorted_locs:
                loc = sorted_locs.pop()[0]
                result.append(loc)
                count += 1
        return result
                
