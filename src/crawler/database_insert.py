'''
Created on May 29, 2012

@author: Tyler
'''
import MySQLdb
import sys
import _mysql_exceptions

"""
This class modifies the database for us.
"""
class database_insert(object):

    """
    Constructs the dbmanager and connects to the database.
    """
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host = "ovid01.u.washington.edu",
                               user = "harshad",
                               passwd = "purple pony disco",
                               db = "know_db"
                               , port= 32002)
        except _mysql_exceptions.OperationalError:
            print "Timeout on connection to the database."
            sys.exit(1)
    
    """
    Reverts user_list back to white_list and clears black_list.
    """        
    def revert_to_white(self):
        q1 = "delete from user_list;"
        self.conn.query(q1)
        q2 = "delete from black_list;"
        self.conn.query(q2)
        q = "select * from white_list;"
        curs = self.conn.cursor()
        curs.execute(q)
        rows = curs.fetchall()
        list = []
        for row in rows:
            list.append(row[0])
#        w = "delete from locations where location like \"%(%\";"
#        self.conn.query(w)
        for item in list:
#            print item
            query = "insert into user_list values(\"" + item + "\");"
            try:
                self.conn.query(query)
            except _mysql_exceptions.IntegrityError:
                print "Already inserted: " + query
        
            
        """
    Closes the connection to the database.
    """    
    def close(self):
        self.conn.close()

db = database_insert()
db.revert_to_white()
db.close()