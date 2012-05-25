"""
Created on Apr 23, 2012

@author: Nolan, Tyler
"""
import WebsiteCrawler
import DBManager
import optparse

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
    print "Dry run: " + str(options.DRY_RUN)
    if options.SOURCE_URL:
        print "Running on " + str(options.SOURCE_URL) + "."
        db = DBManager.DBManager()
        crawler = WebsiteCrawler.WebsiteCrawler()
        results = crawler.parse_articles(crawler.get_links(options.SOURCE_URL))
        for article in results:
            db.add_article_list(article, options.DRY_RUN)
    else:
        print "Running on list of news sources."        
        divisor = int(options.NUM_PROCESSES)
        process_lists = []
        db = DBManager.DBManager()
        rows = db.send_query("select * from user_list")
        counter = 0
        for i in range(0,divisor):
            process_lists.append([])
        for row in rows:
            process_lists[counter % divisor].append(row[0])
            counter += 1
        for i in range(0, divisor):
            __run_from_list(process_lists[i])
    #    rows = db.send_query("select nsource_url from news_sources")

    db.close()

def __run_from_list(websites):
    db = DBManager.DBManager()
    for site in websites:
        crawler = WebsiteCrawler.WebsiteCrawler()
        results = crawler.parse_articles(crawler.get_links(site))
        for article in results:
            db.add_article_list(article, options.DRY_RUN)
        del crawler
  
if __name__ == "__main__":
    (options, args) = parse_arguments()
    main(options)