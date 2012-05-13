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
    Takes a list of words and returns list of unique words and their frequencies.
    """
    def word_frequencies(self, text):
        words = self.word_list(text)
        uniqueWords = set(words)
        return sorted([(words.count(word), word) for word in uniqueWords])
    
    """
    Takes a list of word frequencies and returns numWords of the most
    frequently used words that do no belong to commonWords.
    """
    def top_k_unique_words(self, wordCounts, numWords, commonWords):
        count = 0
        result = []
        while (count < numWords):
            word = wordCounts.pop()
            if commonWords.find(word) == -1:
                result.append(word)
                count += 1


if __name__ == '__main__':
    s1=Utilities()
    s2=Utilities()
    if(id(s1)==id(s2)):
        print "Same"
    else:
        print "Different"
        
u = Utilities()
a = "apple-dog +cat #$%^&*() 1920         42orange  banana dog\ndog's cat's apples, Tyler's dog's apple's cat.dsasdsa\nqwerty:asdfg;zxcv"
b = u.word_frequencies(a)
print b