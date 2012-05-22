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
    Constructs a Utilities object and generates a list of common words.
    """
    def __init__(self):
        self.common_words = []
        rows = DBManager.DBManager().send_query("select * from common_words;")
        for row in rows:
            self.common_word.append(row[0])
    
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
    Takes a list of word frequencies and returns up to numWords of the most
    frequently used words that do no belong to commonWords. Returns
    an empty list if numWords <= 0 or if all of the words in wordCounts
    are found in commonWords.
    """
    def top_k_unique_words(self, word_counts, num_words, common_words):
        result = []
        if num_words > 0:
            count = 0
            while (count < num_words) and word_counts:
                word = word_counts.pop()[1]
                if not (word in common_words):
                    result.append(word)
                    count += 1
        return result


#if __name__ == '__main__':
#    s1=Utilities()
#    s2=Utilities()
#    if(id(s1)==id(s2)):
#        print "Same"
#    else:
#        print "Different"