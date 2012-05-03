'''
Created on Apr 23, 2012

@author: Nolan, Tyler
'''
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
    parser = optparse.OptionParser(description="Process url.")
    parser.add_option("-u", dest="SOURCE_URL",
        help="The url of the news source to be processed.")
    return parser.parse_args()

"""
Crawls the passed arguments url and saves all data to the sql database.
"""
def main(args):
    db = DBManager.DBManager()
    crawler = WebsiteCrawler.WebsiteCrawler()
    if args.SOURCE_URL == None:
        print "knowcrawler.zip: try knowcrawler.zip -u http://www.nytimes.com/"
        
    if args.SOURCE_URL == "http://www.nytimes.com/":
        print args.SOURCE_URL
        results = crawler.parse_articles(crawler.get_links(args.SOURCE_URL))
        for article in results:
            db.add_article_list(article)
        #db.print_database()
    db.close()
  
if __name__ == "__main__":
    (options, args) = parse_arguments()
    main(options)