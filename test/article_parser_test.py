'''
Created on Apr 29, 2012

@author: Tyler
'''
import unittest
import sys
sys.path.append("../src/crawler")
import ArticleParser
#from ..src.crawler import ArticleParser


class Test(unittest.TestCase):


    def test_pre_parse_empty(self):
        self.assertEqual("", ArticleParser.ArticleParser.pre_parse("", "script"))
        
    def test_pre_parse_no_tag(self):
        html = '''<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>'''
        self.assertEqual(html, ArticleParser.ArticleParser.pre_parse(html, "script"))
        
    def test_pre_parse_with_tag(self):
        html = '''<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>'''
        expected = '''<html>
<body>



<p>My first paragraph.</p>

</body>
</html>'''
        self.assertEqual(expected, ArticleParser.ArticleParser.pre_parse(html, "h1"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()