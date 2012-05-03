'''
Created on May 2, 2012

@author: Tyler
'''
import unittest

testmodules = [
    "db_manager_test",
    "article_parser_test",
    "website_crawler_test"]

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