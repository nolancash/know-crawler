"""
Created on May 2, 2012

@author: Ned Batchelder
"""
import unittest

"""
This module runs all of our unit tests.
"""

"""
Takes each unit test and runs them all as a single test.
"""
def main():
    testmodules = [
        "db_manager_test",
        "article_parser_test",
        "website_crawler_test",
        "utilities_test",
        "db_manager_test"]
    
    suite = unittest.TestSuite()
    
    for test in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(test, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
    
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_get_country_list']
    main()