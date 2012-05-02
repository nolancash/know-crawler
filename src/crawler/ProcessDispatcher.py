'''
Created on Apr 23, 2012

@author: Nolan
'''
import WebsiteCrawler
import DBManager
import optparse

#db = DBManager.DBManager()
#
#crawler = WebsiteCrawler.WebsiteCrawler()
#results = crawler.parse_articles(crawler.get_links("http://www.nytimes.com/"))
#
#
#
#for article in results:
#    db.add_article_list(article)
#db.print_database()
#db.close()

def parse_arguments():
    parser = optparse.OptionParser(description="Process url.")
    parser.add_option("-u", dest="SOURCE_URL",
        help="The url of the news source to be processed.")
    return parser.parse_args()

def main(args):
    db = DBManager.DBManager()
    crawler = WebsiteCrawler.WebsiteCrawler()
    print args.SOURCE_URL
    results = crawler.parse_articles(crawler.get_links(args.SOURCE_URL))
    for article in results:
        db.add_article_list(article)
    #db.print_database()
    db.close()
  
if __name__ == "__main__":
    (options, args) = parse_arguments()
    main(options)