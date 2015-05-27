# KNOW-Crawler User Documentation #

**Table of Contents**




---


## What is KNOW-Crawler? ##

The know-crawler is a customizable web crawling tool for the KNOW Project at the University of Washington. The concept is simple: instead of having students manually enter meta-data about articles such as dates, authors, keywords, etc., we automate the process with a web crawler. Our web crawler parses through news articles and compacts meta-data into one useful annotation about each article which we store in our database. The metadata includes the following information for each article: title, description, keywords, author, date, url. Our database of annotations could later be used to produce valuable visualization tools for analyzing news articles about international events.

The concept around which the UI is organized is also very simple. The UI is a website.  The way in which the user performs specific actions is simply by clicking links which will navigate the user throughout the different pages of the website and checking radio buttons or checkboxes to select the desired settings. There will be a default value for each category so if the user doesn't specify a value then the default value will be used for this particular category. Therefore, the input of the user will be always valid. The UI is designed as an analogy to the real world process of ordering food from a delivery website. You log in with
a password and choose the day and time of the delivery. You also select from the list of products the list of items that you want to have delivered. The modes are the default values. There will be a default time the crawler will run - once weekly at 2 am and there will be a default list of news sources that the crawler will crawl that is specified by our customer.  Currently our crawler works only on http://www.nytimes.com/.


---



## How to Install and Run the KNOW-Crawler ##

There is no need to install the KNOW-Crawler.  The crawler is already installed on a UW server, so all you need to do is decide when and what you wish to crawl.  To turn the crawler on, navigate to the settings page [here](http://depts.washington.edu/knowcse2/index.php) and select the "On" radio button. Please note: Only KNOW Project administrators have access to the settings page.


---


## How to Modify Time Settings ##

To view and edit the time settings:

  1. Navigate to the settings page [here](http://depts.washington.edu/knowcse2/index.php) and locate the "Time Schedule" box.
  1. Under "Time", specify the hour of the day (am or pm) you wish for the crawler to run at.
  1. Under "Days", specify which days of the week you wish the crawler to run on.
  1. Click the "Submit" button in the "Time Schedule" box and you're done.
  1. The next time you load the settings page you will see your most recent settings saved to the inputs.



---


## How to Modify Article List ##

To view and edit the news source list:

  1. Navigate to the settings page [here](http://depts.washington.edu/knowcse2/index.php) and locate the "Articles to Crawl" box.
  1. Check all boxes next to news sources you wish to crawl.
  1. Click "Select All" or "Deselect All" to conveniently clear or select the whole list.
  1. When you are satisfied with our list of articles to crawl, click the "Submit" button in the "Articles to Crawl" box.
  1. The next time you load the settings page you will see all the articles currently set to crawl are checked.


---


## Bug Reporting ##

If you encounter problems with KNOW-Crawler, please take a look at the http://code.google.com/p/know-crawler/issues/list issues list to see if other people have already notified us of the problems. If no, please submit your issues there.
When describing the issue, please include the following documentation:

1. Title - the title of the report should give us a rough idea of the issue;

2. Short description - a good description in a professional tone will help us understand the problem;

3. Routing information - needed so that the report is directed to the responsible group; including correct routing info will guarantee faster response; this includes the category (the specific component
tha exhibits the problem) and the severity of the issue;

4. Test case - in order to find the problem and develop a solution we must reproduce the problem exactly. Therefore, please include the following description: operating system and hardware used when the problem occured, steps to reproduce the problem, the expected result,
and the actual result.

5. Contact information - The contact information we need is name, email, and company affiliation if any. This information will help us contact the submitter if we need to communicate with him in order to clarfy some of the submitted information and direct our comments properly.


---
