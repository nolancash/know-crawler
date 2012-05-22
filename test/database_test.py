'''
Created on May 12, 2012

@author: Harshad
'''
import unittest
import sys
sys.path.append("../src/crawler")
from crawler import DBManager
from crawler import Utilities


class Test(unittest.TestCase):


    def test_articles_null(self):
        rows = DBManager.DBManager().send_query("select * from articles where title like 'null';");
        self.assertEqual(len(rows), 0, "no null titles")
        rows = DBManager.DBManager().send_query("select * from articles where description like 'null';");
        self.assertEqual(len(rows), 0, "no null descs")
        pass

#    def test_add_common_words(self):
#        util = Utilities.Utilities()
#        for s in util.common_words:
#            rows = DBManager.DBManager().send_query("select * from common_words where word like '" + s + "';");
#            if len(rows) == 0:
#                query = "insert into common_words values('" + s + "');"
#                DBManager.DBManager().send_query(query)
#        pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()