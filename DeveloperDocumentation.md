# KNOW-Crawler Developer Documentation #

**Table of Contents**




---


## Preface ##

For design structure and decisions, please refer to the Software Design Specification document:

http://code.google.com/p/know-crawler/downloads/detail?name=SDS.pdf

---


## How to Obtain the Source ##

The source for the latest stable version can be found on the Downloads page:

http://code.google.com/p/know-crawler/downloads/detail?name=know-crawler-1.0.1-source.zip

The source code can also be obtained from our mercurial master repository using:

```
hg clone https://code.google.com/p/know-crawler/
```


---


## Directory Structure ##

The following table explains the directory structure of the source code download:

|site|This folder contains all back-end processes related to the schedule settings of the know-crawler.|
|:---|:------------------------------------------------------------------------------------------------|
|public\_html|This folder contains all the php and html for the know-crawler website.                          |
|src |This folder contains all the source code for the webcrawler.                                     |
|test|This folder contains all the unit tests for the webcrawler.                                      |
|know-crawler-1.0.1.zip|This is an executable version of the webcrawler.                                                 |
|README.txt|This provides additional information about the project.                                          |


---


## Setup ##

In order to begin work on the KNOW-Crawler, multiple development tools must be properly installed. You must also be on a Fedora or Red Hat Linux distribution. The following instructions will allow you to replicate the entire system architecture for your own development.  To work on the web crawler module, a Python interpreter is required as well as a few libraries to allow it to interface with the web page and MySQL database.  Additionally, a functional MySQL database should be created to store annotations.  Finally, a web page interface and Cron job are necessary to run the web crawler on a customized schedule.

### Web Crawler Setup ###

1. An IDE is highly recommended: Eclipse provides exceptional development functionality for this project (http://www.eclipse.org/downloads/). A Java install is required for this.

2. Install Python 2.6.6 (http://www.python.org/download/) or greater if it is not installed.

3. Install Mercurial (http://mercurial.selenic.com/). For Eclipse users, a plugin exists (http://javaforge.com/project/HGE).

4. Download the source for Mechanize (http://wwwsearch.sourceforge.net/mechanize/download.html). This is the library needed for webcrawling. Unzip and place the source folder in the same folder that contains the web crawler.

### Database Setup ###

This section will cover the database setup portion of the project. Finishing this section will result in a personal version of the KNOW database, as well as full configuration on the MySql and PHPMyAdmin side to allow the webcrawler to connect to the database. The database is relatively easy to set up on a University of Washington host machine with a provided version of the database, or even making the database from scratch.

1. The instructions given at (http://www.washington.edu/itconnect/web/publishing/students.html#activate_pub) show how to set up web hosting on the UW account that will be using the host machine and database. This will setup Apache web hosting and create a public\_html folder.

2. The instructions given at (http://www.washington.edu/itconnect/web/publishing/mysql-installed.html) indicate how to install and properly configure MySql so that it will work on the host.

3. Finally, the instructions at (http://www.washington.edu/itconnect/web/publishing/phpmyadmin.html) explain how to set up PHPMyAdmin, a simple yet effective tool for using and querying databases in a web browser.

Once all the setup steps have been done, developers can enter MySql and either import an existing copy of the database or create a new one to store all the data brought in by the webcrawler.  The schemas for the various database tables are provided in the SDS. If a new database is being made, these tables can be added using the 'create table' command in MySql.

Next, download a dump of the knowcse2 database from http://code.google.com/p/know-crawler/downloads/detail?name=dump.sql&can=2&q=#makechanges and import the dump into MySql using

```
./bin/mysql < ~/dump.sql
```

This will ensure that all required tables are in place and properly formatted.

#### Allowing Access to Webcrawler ####

Now that the database has been setup and PHPMyAdmin is installed, the next step is to enable database access to the web crawler. This can be done by

1. Logging into PHPMyAdmin using a web browser

2. Click the Databases tab to show databases

3. Click the Check Priveleges button next to the KNOW database

4. Click the Add a New User

5. Enter in the user and hostname that the crawler will be running on, and allow access to all database functionality (check all boxes)

6. Save changes

7. Navigate to the DBManager.py file in the web crawler source and change the url, username, password and port to the one that is configured on the MySQL database.


The webcrawler should now be able to query the database.

### User Interface Setup ###

1. Add Mechanize to the PYTHONPATH by editing the file site/scheduler/run\_crawler.sh. Replace "/rc12/d04/knowcse2/mechanize" with the path to where Mechanize is located.

2. Place all files under the directory public\_html on the web server.

3. Edit crontab on the server to execute the python script site/scheduler/scheduler.py hourly.

4. Install Aptana (http://www.aptana.com). This is an open-source web application IDE. Aptana is recommended for developing KNOW-Crawler website.


---


## About the Crawler ##

Here is how the crawler obtains data:

  * Articles are discerned first by checking the extension on the url to ensure it either has more than 18 characters or contains at least 8 digits. In these cases, articles are found in approximately 90% of urls. To further distinguish articles we check to ensure that each page has a title, description, and url field and the type of the page is labeled "article" or "null". In these cases, less than 1% of pages remaining were not articles.

  * The title is discerned by parsing the title tag of an article.

  * The description, author, and type of webpage (article vs. indexing page) are all discerned by parsing their respective meta tags.

  * The keywords are discerned through both the meta tag labeled as "keywords" as well as using a word frequency analysis to determine the most frequently occuring uncommon words. All keywords are comma-separated and lowercase.

  * The locations are discerned by parsing the body text for any reference to a location in our database and using frequency anaylsis to determine the top 4 locations.

  * The time of submission is discerned using the date object built into MySql.

As of May 30, 2012, there are 66 news sources that the webcrawler will run on. The approximate run time of the crawler is 20 minutes using 4 processes.


---


## How to Run the Crawler ##

Because the web crawler uses Python no source code needs to be compiled in order to run the crawler.

1. Obtain the source for the latest stable version (see above).

2. Unzip the source download. This will create a folder called know-crawler at the destination.

3. Navigate to the know-crawler/ folder via command prompt.

4. Typing the following command will start the webcrawler for all news sources currently listed in the database:

```
python know-crawler-1.0.1.zip -p 4
```

4a. You may also enter the following command to run the webcrawler but not insert articles into the database:

```
python know-crawler-1.0.1.zip -p 4 -d
```

4b. You may instead enter the following command for additional information:

```
python know-crawler-1.0.1.zip --help
```


---


## How to Test the Crawler ##

1. Obtain the source for the latest stable version (see above).

2. Unzip the source download. This will create a folder called know-crawler at the destination.

3. Navigate to the know-crawler/test/ folder via command prompt.

4. Typing the following command will run all unit tests (test time varies in length due to advertisements on http://www.nytimes.com/ ):

```
python run_tests.py
```


---


## Releasing a New Version ##

1. Run all unit tests to ensure that the new release has not lost functionality and is stable.

2. Zip up the know-crawler/src folder.

3. Email a committer to request permission to push changes to the master repository.


---


## Bug Tracking ##

All past and present issues are tracked at http://code.google.com/p/know-crawler/issues/list.

New bug reports may be submitted by clicking the "New Issue" button and submitting a report.

---
