'''
Created on Apr 27, 2012

@author: Nolan
'''
import MySQLdb

class DBManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.conn = MySQLdb.connect(host = "ovid.u.washington.edu",
                           user = "harshad",
                           passwd = "purple pony disco",
                           db = "know_db"
                           , port= 32001)
    def get_country_list(self):
        self.conn.query("select cntry_name from world_countries;")
        r = self.conn.store_result()
        res = []
        for row in r.fetch_row(0):
            res.append(row[0])
        return res
    
    def close(self):
        self.conn.close()
    
    def add_article_info(self, title, description, keywords, author, date, url):
        query = "insert into articles values(0, \"" + title + "\", \"" + description +"\", \"" + keywords + "\", \"" + author + "\", \"" + date + "\", \"" + url + "\")";
        print query
        self.conn.query(query)
        
    def add_article_list(self, article):
        query = "select * from articles a where a.url = \"" + article[6] + "\";"
        self.conn.query(query)
        r = self.conn.store_result()
        for row in r.fetch_row(0):
            print row
        if len(r.fetch_row(0)) == 0:
            self.add_article_info(article[0], article[1], article[2], article[3], article[4], article[6])
    
    def print_database(self):
        self.conn.query("select * from articles;")
        r = self.conn.store_result()
        res = []
        for row in r.fetch_row(0):
            res.append(row[0])
            print row
#        for q in res:
#            print q

#db = DBManager()
#db.get_country_list()
#
#db.add_article_info("testing stuff", "Null", "null", "mariah cary, iguana, harshad", "11.12.11", "null")
#db.print_database()
#db.close()