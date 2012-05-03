'''
Created on Apr 29, 2012

@author: Tyler
'''
import unittest
import sys
sys.path.append("../src/crawler")
import ArticleParser

'''
This class runs our unit tests for ArticleParser.py.
'''
class Test(unittest.TestCase):

    '''
    Tests pre_parse given an empty parameter.
    '''
    def test_pre_parse_empty(self):
        self.assertEqual("", ArticleParser.ArticleParser.pre_parse("", "script"))
    
    '''
    Tests pre_parse given that the tag given is not found
    in the xhtml.
    '''    
    def test_pre_parse_no_tag(self):
        html = '''<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>'''
        self.assertEqual(html, ArticleParser.ArticleParser.pre_parse(html, "script"))
    
    '''
    Tests pre_parse to ensure that it removes a single tag
    as intended.
    '''    
    def test_pre_parse_one_tag(self):
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
    
    '''
    Tests pre_parse to ensure that it removes multiple
    tags as intended.
    '''    
    def test_pre_parse_multiple_tags(self):
        html = '''<html>
<body>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
<h2>This is a dummy tag</h2>
<h1>To be removed</h1><p>Keep this</p><h1>Delete this</h1>
</body>
</html>'''
        expected = '''<html>
<body>

<p>My first paragraph.</p>
<h2>This is a dummy tag</h2>
<p>Keep this</p>
</body>
</html>'''
        self.assertEqual(expected, ArticleParser.ArticleParser.pre_parse(html, "h1"))
    
    '''
    Tests get_html given an empty parameter.
    '''    
    def test_get_html_empty_url(self):
        result = ArticleParser.ArticleParser().get_html("")
        self.assertEqual("", result)
    
    '''
    Tests get_html given an invalid, non-existent url.
    '''
    def test_get_html_invalid_url(self):
        result = ArticleParser.ArticleParser().get_html("http://thisurldoesntexist.net/")
        self.assertEqual("", result)
    
    '''
    Tests get_html given a valid url.
    Note: If this test fails check to make sure the page 
    itself has not changed. This tests checks the xhtml of
    http://www.cs.washington.edu/education/courses/cse403/11sp/old-exams/
    '''    
    def test_get_html_valid_url(self):
        expected = '''<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html 
PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
<meta http-equiv="content-style-type" content="text/css" />
<meta name="MSSmartTagsPreventParsing" content="true" />
<link href="../css/default.css" rel="stylesheet" type="text/css" />
<title>Old CSE 403 exams</title>
</head>

<body>
<!-- beginning of header.html -->
<div id="header">
<div id="logoBar">
<img src="../img/fountain.png" alt="UW Fountain" title="UW Fountain" /><img src="../img/uw-logo.gif" alt="UW logo" title="UW logo" />
</div>

<div id="topNav">
<a href="http://www.washington.edu/uwin/">University of Washington</a>
<a href="http://www.cs.washington.edu/">Computer Science and Engineering</a>
</div>

<div id="classLink">
<a href="http://www.cs.washington.edu/education/courses/cse403/11sp/">CSE 403, Software Engineering</a>
</div>
</div>
<!-- end of header.html -->

<!-- beginning of sideNav.html -->
<div id="sideNav">
<h1>CSE 403</h1>
<a href="../index.html">Home</a>

<h2>Classwork</h2>
<a href="../calendar403.html">Calendar</a>
<a href="../lectures/">Lectures</a>
<a href="../assignments/">Assignments</a>
<a href="https://catalyst.uw.edu/collectit/dropbox/punya/15102">Turn-in</a>
<a href="../projects403.html">Projects</a>
<a href="../software403.html">Software Tools</a>
<a href="../resources403.html">Resources</a>
<a href="../old-exams/">Old exams</a>

<h2>Administration</h2>
<a href="../syllabus403.html">Syllabus</a>
<a href="../grading403.html">Grading</a>
<a href="http://www.cs.washington.edu/education/AcademicMisconduct/">Academic&nbsp;Conduct</a>
<a href="http://www.washington.edu/students/gencat/front/Disabled_Student.html">Accommodations</a>

<h2>Communication</h2>

<a href="https://catalyst.uw.edu/gopost/board/punya/21533/">Forum</a>
<a href="https://cubist.cs.washington.edu/wiki/index.php/CSE403_Spring_2011">Wiki</a>
<a href="http://mailman1.u.washington.edu/mailman/private/cse403a_sp11/">Email archives</a>
</div>
<!-- end of sideNav.html -->


<div id="pageBody">

<h1>Old CSE 403 exams</h1>

<ul>
  <li><a href="05su-midterm.pdf">2005 summer midterm solutions</a></li>
  <li><a href="05su-final.pdf">2005 summer final</a></li>
  <li><a href="06sp-final.pdf">2006 spring final</a></li>
  <li><a href="06su-midterm.pdf">2006 summer midterm solutions</a></li>
  <li><a href="06su-final.pdf">2006 summer final</a></li>
  <li><a href="07wi-final.pdf">2007 winter final</a></li>
  <li><a href="07sp-final.pdf">2007 spring final</a></li>
  <!-- Winter 2008: instructor requests that exam not be posted. -->
  <!-- Spring 2008: instructor requests that exam not be posted. -->
  <li><a href="09sp-final.pdf">2009 spring final</a></li>
  <li><a href="09sp-final-solutions.pdf">2009 spring final solutions</a></li>
  <li><a href="11wi-midterm.pdf">2011 winter midterm</a></li>
  <li><a href="11wi-midterm-solution.pdf">2011 winter midterm solutions</a></li>
  <li><a href="11sp-midterm.pdf">2011 spring midterm</a></li>
  <li><a href="11sp-midterm-solutions.pdf">2011 spring midterm solutions</a></li>
  <li><a href="11sp-final.pdf">2011 spring final</a></li>
  <li><a href="11sp-final-solutions.pdf">2011 spring final solutions</a></li>
</ul>

<p>
We recommend that you do not use these exams to prepare for your own
exam. Instead, use them to <em>evaluate</em> your preparation. That is, you
should first study as you ordinarily would, without looking at the
exams. Then, take an exam: actually write out all the answers. Finally,
grade yourself by use of the solutions key. If you did not get all the
answers right, then you didn't understand the material, and should study
more. It's important to learn the concept behind a wrong answer, but
&mdash; equally importantly &mdash; to think about what other concepts you
might also have overlooked and adjust your studying style.
</p>

<p>
An all-too-common alternative approach is to skim over the exam solutions,
and tell yourself that yes, you could have answered that question (without
actually trying to answer it). This approach is much less successful, and
we do not recommend it.
</p>

</div>

<!-- beginning of footer.html -->
<div id="footer">
<div>Last modified: Tuesday, 28-Jun-2011 07:59:51 PDT</div>

<!--
<div class="w3c">
  <p style="float: left">
    <a href="http://validator.w3.org/check/referer"><img style="border:0;width:88px;height:31px" src="http://www.w3.org/Icons/valid-xhtml10-blue" alt="Valid XHTML 1.0 Strict" /></a>

    <a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!" /></a>
    </p>

</div>
-->

<!-- end of footer.html -->


</body>
</html>

'''
        actual = ArticleParser.ArticleParser().get_html("http://www.cs.washington.edu/education/courses/cse403/11sp/old-exams/")
        self.assertEqual(expected, actual)        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()