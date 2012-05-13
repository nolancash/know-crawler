"""
Created on Apr 30, 2012

@author: Tyler
"""
import unittest
import sys
sys.path.append("../src/crawler")
from crawler import WebsiteCrawler

"""
This class runs our unit tests for WebsiteCrawler.py.
Note: We are testing our data using http://www.nytimes.com/.
Expect some delay in the tests as the source has longer loading
times due to advertisements.
"""
class Test(unittest.TestCase):

    """
    Tests get_links given and empty parameter.
    """
    def test_get_links_empty(self):
        self.assertEqual(None, WebsiteCrawler.WebsiteCrawler().get_links(""))

    """
    Tests get_links to ensure that it is grabbing enough links.
    We know for a fact that there should always be at least
    30 links on the front page of http://www.nytimes.com/.
    """
    def test_get_links_size(self):
        articles = WebsiteCrawler.WebsiteCrawler().get_links(
                    "http://www.nytimes.com/")
        self.assertTrue(len(articles) > 30);
    
    """
    Tests get_links to ensure that each link on the front page
    of http://www.nytimes.com/ belongs to nytime.com and does
    not contain references to other websites.
    """
    def test_get_links_quality(self):
        articles = WebsiteCrawler.WebsiteCrawler().get_links(
                    "http://www.nytimes.com/")
        for article in articles:
            self.assertTrue(article.find("http://www.nytimes.com/") != -1)
    
    """
    Tests parse_articles given an empty parameter.
    """
    def test_parse_articles_empty(self):
        self.assertEqual([], WebsiteCrawler.WebsiteCrawler().parse_articles(""))
    
    """
    Tests parse_articles on the links given by the front
    page of http://www.nytimes.com/. We know for a fact
    that there should be at least 30 articles with proper
    data being parsed.
    """    
    def test_parse_articles_normal(self):
        articles = WebsiteCrawler.WebsiteCrawler().get_links(
                    "http://www.nytimes.com/")
        results = WebsiteCrawler.WebsiteCrawler().parse_articles(articles)
        self.assertTrue(len(results) > 30)
#    
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