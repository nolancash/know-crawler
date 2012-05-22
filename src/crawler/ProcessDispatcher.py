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
#    parser.add_option("-u", dest="SOURCE_URL",
#        help="The url of the news source to be processed.")
    parser.add_option("-d", action="store_true", dest="DRY_RUN", default=False,
                      help="Does a dry run by not inserting articles into the database.")
    return parser.parse_args()

"""
Crawls the passed arguments url and saves all data to the sql database.
"""
def main(options):
    print "Dry run: " + str(options.DRY_RUN)
    db = DBManager.DBManager()
    crawler = WebsiteCrawler.WebsiteCrawler()
#    if options.SOURCE_URL == None:
#        print "knowcrawler.zip: try knowcrawler.zip -u http://www.nytimes.com/"
        
#    print options.SOURCE_URL
    divisor = 1
    rows = db.send_query("select nsource_url from news_sources")
    pages2crawl = len(rows) / divisor
    pagesCrawled = 0
    for row in rows:
        if pagesCrawled == pages2crawl:
            break
        pagesCrawled += 1
        print row[0]
        results = crawler.parse_articles(crawler.get_links(row[0]))
        for article in results:
            db.add_article_list(article, options.DRY_RUN)
                #db.print_database()
                
#    results = crawler.parse_articles(crawler.get_links(options.SOURCE_URL))
#    if options.DRY_RUN:
#            print "Regular run."
#            for article in results:
#                db.add_article_list(article)
    
#    else:
#        print "Dry Run."
#        #db.print_database()
    db.close()
  
if __name__ == "__main__":
    (options, args) = parse_arguments()
    main(options)