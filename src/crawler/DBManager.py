"""
Created on Apr 27, 2012

@author: Nolan, Tyler, Harshad
"""
import MySQLdb
import cgi

"""
This class handles all interaction with the mysql database including but not limited to adding article summaries
to the database.
"""
class DBManager(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBManager, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    """
    Constructs the dbmanager and connects to the database.
    """
    def __init__(self):
        self.conn = MySQLdb.connect(host = "ovid.u.washington.edu",
                           user = "harshad",
                           passwd = "purple pony disco",
                           db = "know_db"
                           , port= 32001)
        
    """
    Retrieves a list of all countries in the world from the database and returns them as a list 
    of strings.
    """
    def get_country_list(self):
        self.conn.query("select cntry_name from world_countries;")
        r = self.conn.store_result()
        res = []
        for row in r.fetch_row(0):
            res.append(row[0])
        return res

    """
    Closes the connection to the database.
    """    
    def close(self):
        self.conn.close()
    
    """
    Adds the passed strings title, description, keywords, author date and url to the database but only if 
    the passed title, description and keywords have values that are != "null".
    """
    def add_article_info(self, title, description, keywords, author, url, dry_run, location):
        if title != "null" and description != "null" and url != "null":
            query = "insert into articles values(0, \"" + cgi.escape(title, True) + "\", \""
            query += cgi.escape(description, True) +"\", \"" + cgi.escape(keywords, True)
            query += "\", \"" + cgi.escape(author, True) + "\", NOW(), \"" + cgi.escape(url, True) + "\", 'null', 'null')"
            print query
            if not dry_run:
                self.conn.query(query)
                query = "insert into locations values('" + cgi.escape(location, True) + "')"
                self.conn.query(query)
                return True
        return False
    
    """
    Takes a list of article summaries and adds them into the database. each list element must be a list with this format 
    ["title", "description", "keywords", "author", "url"] and the first 3 elements must not equal "null". The
    Passed url of each article summary must not already exist in the database as well.
    """   
    def add_article_list(self, article, dry_run):         
        if len(article) == 6 and (article[4].lower() == "article" or article[4] == "null"):
            query = "select * from articles a where a.url like \"%" + article[5] + "%\";"
            curs = self.conn.cursor()
            curs.execute(query)
            rows = curs.fetchall()
            if len(rows) == 0:
                return self.add_article_info(article[0], article[1], article[2], article[3], article[5], dry_run)
            else:
                print "Article already in database: " + article[5]
        return False
    
    """
    Prints out all article summaries that are stored in the database.
    """
    def print_database(self):
        self.conn.query("select * from articles;")
        r = self.conn.store_result()
        res = []
        for row in r.fetch_row(0):
            res.append(row[0])
            print row
            
    def send_query(self, query = "select * from articles;"):
        curs = self.conn.cursor()
        curs.execute(query)
        rows = curs.fetchall()
        return rows
