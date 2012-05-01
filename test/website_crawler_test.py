'''
Created on Apr 30, 2012

@author: Tyler
'''
import unittest
import mechanize
import sys
sys.path.append("../src/crawler")
import WebsiteCrawler


class Test(unittest.TestCase):


    def test_get_links(self):
        self.assertTrue(len(
            WebsiteCrawler.WebsiteCrawler().get_links(
            "http://www.nytimes.com/")) > 30);
    
#    def test_get_links_disallow_robots(self):
#        url = "http://www.nytimes.com/reuters/2012/04/30/sports/golf/30reuters-golf-european.html";
#        try:
#            WebsiteCrawler.WebsiteCrawler().get_links(url)
#            self.fail("Didn't raise error.")
#        except Exception, e:
#            error = str(e)
#            self.assertEqual("HTTP Error 403: request disallowed by robots.txt", error)
#    
#    def test_parse_articles_disallow_robots(self):
#        url = ["http://www.nytimes.com/reuters/2012/04/30/sports/golf/30reuters-golf-european.html"];
#        try:
#            WebsiteCrawler.WebsiteCrawler().parse_articles(url)
#            self.fail("Didn't raise error.")
#        except Exception, e:
#            error = str(e)
#            self.assertEqual("HTTP Error 403: request disallowed by robots.txt", error)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_get_links']
    unittest.main()