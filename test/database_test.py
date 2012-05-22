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


    def test_articles(self):
        rows = DBManager.DBManager().send_query("select * from articles where title like 'null';");
        self.assertEqual(len(rows), 0, "no null titles")
        rows = DBManager.DBManager().send_query("select * from articles where description like 'null';");
        self.assertEqual(len(rows), 0, "no null descs")
        pass
    
    def test_common_words(self):
        rows = DBManager.DBManager().send_query("select * from common_words where word like 'null';");
        self.assertEqual(len(rows), 0, "no null words")
        pass
    
    def test_user_list(self):
        rows = DBManager.DBManager().send_query("select * from user_list where url like 'null';");
        self.assertEqual(len(rows), 0, "no null urls")
        pass
    
    def test_white_list(self):
        rows = DBManager.DBManager().send_query("select * from white_list where url like 'null';");
        self.assertEqual(len(rows), 0, "no null urls")
        pass
    
    def test_black_list(self):
        rows = DBManager.DBManager().send_query("select * from black_list where url like 'null';");
        self.assertEqual(len(rows), 0, "no null urls")
        pass
    
    def test_full_list(self):
        rows = DBManager.DBManager().send_query("select * from news_sources where nsource_url like 'null';");
        self.assertEqual(len(rows), 0, "no null urls")
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