'''
Created on May 12, 2012

@author: Harshad
'''
import unittest
import sys
sys.path.append("../src/crawler")
from crawler import DBManager


class Test(unittest.TestCase):


    def test_articles_null(self):
        rows = DBManager.DBManager().send_query("select * from articles where title like 'null';");
        self.assertEqual(len(rows), 0, "no null titles")
        rows = DBManager.DBManager().send_query("select * from articles where description like 'null';");
        self.assertEqual(len(rows), 0, "no null descs")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()