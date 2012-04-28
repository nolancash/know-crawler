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
        r = db.conn.store_result()
        res = []
        for row in r.fetch_row(0):
            res.append(row[0])
        return res
    
    def close(self):
        self.conn.close()
    
    def add_article_info(self, url, title, description, keywords, date, author):
        query = "insert into articles values(0, \"" + title + "\", \"" + description +"\", \"" + keywords + "\", \"" + author + "\", \"" + date + "\", \"" + url + "\")";
        print query
        self.conn.query(query)

db = DBManager()
db.get_country_list()
db.add_article_info("null", "null", "null", "mariah cary, iguana, harshad", "11.12.11", "null")
db.close()