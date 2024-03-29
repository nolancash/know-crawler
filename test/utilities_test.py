'''
Created on May 12, 2012

@author: Tyler
'''
import unittest
import sys
sys.path.append("../src/crawler")
import Utilities

"""
This class runs our unit tests for Utilities.py.
"""
class Test(unittest.TestCase):

    """
    Tests word_list given no text with ignoreCase on.
    """
    def test_word_list_empty(self):
        self.assertEqual([], Utilities.Utilities().word_list("", True))
    
    """
    Tests word_list given no text with ignoreCase off.
    """
    def test_word_list_empty_ignore(self):
        self.assertEqual([], Utilities.Utilities().word_list("", False))
    
    """
    Tests word_list with "simple" ASCII text.
    """    
    def test_word_list_normal(self):
        s = "The brown fox jumped over the lazy dog. Dog ate cat and fox, winner."
        expected = ["the", "brown", "fox", "jumped", "over", "the",
                    "lazy", "dog", "dog", "ate", "cat", "and", "fox", "winner"]
        self.assertEqual(expected, Utilities.Utilities().word_list(s, True))
        
    """
    Tests word_list with numbers formatted with commas.
    """    
    def test_word_list_numbers(self):
        s = "The brown fox jumped over the lazy dog. Dog ate cat and fox, winner. 100,000 100,000"
        expected = ["the", "brown", "fox", "jumped", "over", "the",
                    "lazy", "dog", "dog", "ate", "cat", "and", "fox", "winner", "100000", "100000"]
        self.assertEqual(expected, Utilities.Utilities().word_list(s, True))
    
    """
    Tests word_list with more ASCII characters.
    """    
    def test_word_list_more_chars(self):
        s = """apple's trees, ,..," candy 1984 &%^$dog"""
        expected = ["apples", "trees", "candy", "1984", "dog"]
        self.assertEqual(expected, Utilities.Utilities().word_list(s, True))
    
    """
    Tests word_frequencies given no text.
    """    
    def test_word_frequencies_empty(self):
        self.assertEqual([], Utilities.Utilities().word_frequencies(""))
        
    """
    Tests word_frequencies given a single word for text.
    """    
    def test_word_frequencies_single_word(self):
        s = "apple"
        expected = [(1, "apple")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
        
    """
    Tests word_frequencies given a "simple" ASCII string.
    """    
    def test_word_frequencies_normal(self):
        s = "The brown fox jumped over the lazy dog. Dog ate cat and fox, winner."
        expected = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
    
    """
    Tests word_frequencies with more ASCII characters.
    """
    def test_word_frequencies_more_chars(self):
        s = """apple's trees, ,..," candy 1984 &%^$dog"""
        expected = [(1, "1984"), (1, "apples"), (1, "candy"), (1, "dog"), (1, "trees")]
        self.assertEqual(expected, Utilities.Utilities().word_frequencies(s))
    
    """
    Tests top_k_unique_words given no word counts.
    """
    def test_top_k_words_empty(self):
        self.assertEqual([], Utilities.Utilities().top_k_words([], 0, []))
        
    """
    Tests top_k_unique_words given a negative value for the number of words.
    """    
    def test_top_k_words_negative_words(self):
        counts = [(1, "apple")]
        self.assertEqual([], Utilities.Utilities().top_k_words(counts, -5, []))
    
    """
    Tests top_k_unique_words without a list of common words.
    """    
    def test_top_k_words_without_common(self):
        counts = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = ["the", "fox", "dog", "winner", "over"]
        self.assertEqual(expected, Utilities.Utilities().top_k_words(counts, 5, []))
    
    """
    Tests top_k_unique_words with a list of common words that intersection a portion of
    the list.
    """
    def test_top_k_words_with_common(self):
        common_words = ["the", "and", "dog", "cat"]
        counts = [(1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = ["fox", "winner", "over", "lazy"]
        self.assertEqual(expected, Utilities.Utilities().top_k_words(counts, 5, common_words))
    
    """
    Tests top_k_unique_words with a list of common words such that the list of word
    frequencies is a subset of the common words.
    """
    def test_top_k_words_with_all_common(self):
        common_words = ["the", "and", "dog", "cat", "ate", "brown", "jumped", "lazy", "over", "winner", "fox"]
        counts = [(1, "and"), (1, "ate"), (1, "brown"), (1, "cat"), (1, "jumped"),
                    (1, "lazy"), (1, "over"), (1, "winner"), (2, "dog"), (2, "fox"), (2, "the")]
        expected = []
        self.assertEqual(expected, Utilities.Utilities().top_k_words(counts, 5, common_words))
        
    """
    Tests get_locations with given no text.
    """
    def test_get_locations_empty(self):
        self.assertEqual({}, Utilities.Utilities().get_locations("", []))
    
    """
    Tests get_locations given no locations to parse.
    """  
    def test_get_locations_no_locations(self):
        text = "This is a sample string with no locations."
        self.assertEqual({}, Utilities.Utilities().get_locations(text, []))
    
    """
    Tests get_locations given a normal text body and a list of locations.
    """   
    def test_get_locations_normal(self):
        text = "This is a story about the democratic england America and the english England england England trinidad and tobago."
        locs = ["America", "Canada", "England", "Trinidad and Tobago", "The Democratic Republic of the Congo", "Australia"]
        expected = {"trinidad and tobago": 1, "america": 1, "england": 4}
        self.assertEqual(expected, Utilities.Utilities().get_locations(text, locs))
    
    """
    Tests top_k_locations given no location dictionary.
    """
    def test_top_k_locations_empty(self):
        self.assertEqual([], Utilities.Utilities().top_k_locations({}, 0))
        
    """
    Tests top_k_locations with no max value given.
    """    
    def test_top_k_locations_no_max(self):
        locs_dict = {'trinidad and tobago': 1, 'america': 1, 'england': 4}
        self.assertEqual([], Utilities.Utilities().top_k_locations(locs_dict, 0))
       
    """
    Tests top_k_locations on a normal dictionary of locations and a maximum
    value less than the number of locations.
    """ 
    def test_top_k_locations_normal(self):
        locs_dict = {'trinidad and tobago': 1, 'america': 1, 'england': 4}
        expected = ["england", "trinidad and tobago"]
        self.assertEqual(expected, Utilities.Utilities().top_k_locations(locs_dict, 2))
    
    """
    Tests top_k_locations with the maximum number of locations greater than the
    total number of locations in the dictionary.
    """
    def test_top_k_locations_greater_max(self):
        locs_dict = {'trinidad and tobago': 1, 'america': 1, 'england': 4}
        expected = ["england", "trinidad and tobago", "america"]
        self.assertEqual(expected, Utilities.Utilities().top_k_locations(locs_dict, 10))
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()