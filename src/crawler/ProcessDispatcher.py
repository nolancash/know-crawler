"""
Created on Apr 23, 2012

@author: Nolan, Tyler
"""
import WebsiteCrawler
import DBManager
import optparse
import sys
import datetime
import TimeoutException
import os
from multiprocessing import Pool

"""
This script runs the web crawler. In future releases it will also manage the multiprocessing of the crawler.
"""

"""
Parses out the passed arguments for the url to be crawled.
"""
def parse_arguments():
    parser = optparse.OptionParser(description="know-crawler-0.1.1")
    parser.add_option("-u", dest="SOURCE_URL",
        help="The url of the news source to be processed.")
    parser.add_option("-d", action="store_true", dest="DRY_RUN", default=False,
                      help="Does a dry run by not inserting articles into the database.")
    parser.add_option("-p", dest="NUM_PROCESSES", default=1,
                      help="Declare number of processes to be used.")
    return parser.parse_args()

"""
Crawls the passed arguments url and saves all data to the sql database.
"""
def main(options):
    # Redirects standard output to a log file.
    log_dir = "crawler_logs"
    log_name = __log_file_name()
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    os.chdir("./" + log_dir + "/")
    os.makedirs(log_name)
    os.chdir("./" + log_name + "/")
    
    if options.SOURCE_URL:
        print "Running on " + str(options.SOURCE_URL) + "."
        db = DBManager.DBManager()
        crawler = WebsiteCrawler.WebsiteCrawler()
        results = crawler.parse_articles(crawler.get_links(options.SOURCE_URL))
        for article in results:
            db.add_article_list(article, options.DRY_RUN)
    else:     
        divisor = int(options.NUM_PROCESSES)
        process_lists = []
        db = DBManager.DBManager()
#        rows = db.send_query("select nsource_url from news_sources")
        rows = db.send_query("select * from user_list")
        counter = 0
        for i in range(0,divisor):
            process_lists.append([options.DRY_RUN, i])
        for row in rows:
            process_lists[counter % divisor].append(row[0])
            counter += 1
#        for i in range(0, divisor):
#            __run_from_list(process_lists[i])
        pool = Pool(processes=divisor)
        pool.map(__run_from_list, process_lists)  
        db.close()

def __run_from_list(websites):
    dry_run = websites.pop(0)
    log_id = str(websites.pop(0))
    
    if len(websites) > 0:
            
        sys.stdout = open("log_" + log_id + ".txt" , "w")
    
        print "Dry run: " + str(dry_run)
        print "Running on list of news sources."   
        
        db = DBManager.DBManager()
        for site in websites:
            print site
            crawler = WebsiteCrawler.WebsiteCrawler()
            links = crawler.get_links(site)
            try:
                results = crawler.parse_articles(links)
            except TimeoutException.TimeoutException:
                print "Timeout Exception (outer)."
            if results:
                for article in results:
                    db.add_article_list(article, dry_run)
            del crawler
        
        db.close()
        print "\nDone."

"""
Concatenates the file name for the log file in the format:
log_yyyy-mm-dd_hh.mm.ss.txt
"""
def __log_file_name():
    date = datetime.datetime.now().replace(microsecond = 0)
    date = str(date)
    date = date.replace(" ", "_")
    date = date.replace(":", ".")
    return "log_" + date
    
  
if __name__ == "__main__":
    (options, args) = parse_arguments()
    main(options)