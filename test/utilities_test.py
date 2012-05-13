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
        
    def test_word_frequencies_empty(self):
        self.assertEqual([], Utilities.Utilities().word_frequencies(""))
        
    def test_word_frequencies_single_word(self):
        s = "apple"
        expected = [(1, "apple")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
        
    def test_word_frequencies_normal(self):
        s = "The brown fox jumped over the lazy dog. Dog ate cat and fox, winner."
        expected = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
    
    def test_word_frequencies_more_chars(self):
        s = """apple's trees, ,..," candy 1984 &%^$dog"""
        expected = [(1, "1984"), (1, "apples"), (1, "candy"), (1, "dog"), (1, "trees")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
    
    def test_top_k_unique_words_empty(self):
        self.assertEqual([], Utilities.Utilities().top_k_unique_words([], 0, []))
        
    def test_top_k_unique_words_negative_words(self):
        counts = [(1, "apple")]
        self.assertEqual([], Utilities.Utilities().top_k_unique_words(counts, -5, []))
        
    def test_top_k_unique_words_without_common(self):
        counts = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = ["the", "fox", "dog", "winner", "over"]
        self.assertEqual(expected, Utilities.Utilities().top_k_unique_words(counts, 5, []))
    
    def test_top_k_unique_words_with_common(self):
        print "starting"
        commonWords = ["the", "and", "dog", "cat"]
        counts = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = ["fox", "winner", "over", "lazy", "jumped"]
        self.assertEqual(expected, Utilities.Utilities().top_k_unique_words(counts, 5, commonWords))
    
    def test_top_k_unique_words_with_all_common(self):
        print "starting"
        commonWords = ["the", "and", "dog", "cat", "ate", "brown", "jumped", "lazy", "over", "winner", "fox"]
        counts = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = []
        self.assertEqual(expected, Utilities.Utilities().top_k_unique_words(counts, 5, commonWords))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()