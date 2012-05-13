'''
Created on May 9, 2012

@author: Tyler, Nolan
'''

import re

class Utilities(object):
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
    def word_list(self, text, ignoreCase = True):    
        # Changes all text to lowercase.
        if ignoreCase:
            text = text.lower()
    
        # Removes ASCII apostrophes from the text.
        text = text.replace("'", "")
        
        # Replaces all non-word character with spaces to represent word boundaries.
        rx = re.compile("[^\w ]")
        text = rx.sub(" ", text)
        
        # Splits words that are divided by spaces.
        text = text.split()
        
        # If any "empty words" have been manufactured by previous processes, drop them.
        text = [x for x in text if x != ""]
        return text
    
    """
    Takes a string of text and returns list of unique words and their frequencies.
    """
    def word_frequencies(self, text):
        words = self.word_list(text)
        uniqueWords = set(words)
        return sorted([(words.count(word), word) for word in uniqueWords])
    
    """
    Takes a list of word frequencies and returns numWords of the most
    frequently used words that do no belong to commonWords. Returns
    an empty list if numWords <= 0 or if all of the words in wordCounts
    are found in commonWords.
    """
    def top_k_unique_words(self, wordCounts, numWords, commonWords):
        result = []
        if numWords > 0:
            count = 0
            while (count < numWords) and wordCounts:
                word = wordCounts.pop()[1]
                print wordCounts
                if not (word in commonWords):
                    print word
                    result.append(word)
                    count += 1
                    print count
        return result


if __name__ == '__main__':
    s1=Utilities()
    s2=Utilities()
    if(id(s1)==id(s2)):
        print "Same"
    else:
        print "Different"