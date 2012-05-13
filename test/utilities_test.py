'''
Created on May 12, 2012

@author: Tyler
'''
import unittest
import sys
sys.path.append("../src/crawler")
import Utilities

class Test(unittest.TestCase):


    def test_word_list_empty(self):
        self.assertEqual([], Utilities.Utilities().word_list("", True))
        
    def test_word_list_empty_ignore(self):
        self.assertEqual([], Utilities.Utilities().word_list("", False))
        
    def test_word_list_normal(self):
        s = "The brown fox jumped over the lazy dog. Dog ate cat and fox, winner."
        expected = ["the", "brown", "fox", "jumped", "over", "the",
                    "lazy", "dog", "dog", "ate", "cat", "and", "fox", "winner"]
        self.assertEqual(expected, Utilities.Utilities().word_list(s, True))
        
    def test_word_list_more_chars(self):
        s = """apple's trees, ,..," candy 1984 &%^$dog"""
        expected = ["apples", "trees", "candy", "1984", "dog"]
        self.assertEqual(expected, Utilities.Utilities().word_list(s, True))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()