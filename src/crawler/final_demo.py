'''
Created on May 30, 2012

@author: Tyler
'''
import MySQLdb
import _mysql_exceptions
import sys
import optparse

"""
This script is a simple demonstration of how easy it is to 
query our database to find articles that have common keywords
or locations and time.
"""
    
"""
Parses out the passed arguments.
Select only one parameter.
"""
def parse_arguments():
    parser = optparse.OptionParser(description="final-demo")
    parser.add_option("-k", dest="KEYWORDS",
        help="The keywords to be parsed for in the article database.")
    parser.add_option("-l", dest="LOCATIONS",
        help="The locations to be parsed for in the article database.")
    parser.add_option("-s", dest="DATE_START",
        help="The dates to be filtered.")
    parser.add_option("-e", dest="DATE_END",
        help="The dates to be filtered.")
    return parser.parse_args()

def main(options):
    try:
        conn = MySQLdb.connect(host = "ovid01.u.washington.edu",
                           user = "harshad",
                           passwd = "purple pony disco",
                           db = "know_db"
                           , port= 32002)
    except _mysql_exceptions.OperationalError:
        print "Timeout on connection to the database."
        sys.exit(1)
    item = ""
    words = []
    if options.KEYWORDS:
        item = "keywords"
        words = options.KEYWORDS.split(" ")
    elif options.LOCATIONS:
        item = "primary_locations"
        words = options.LOCATIONS.split(" ")
    else:
        print "Please rerun with either the -k keywords or -l locations parameter."
    query = "select * from articles"
    count = 0
    #if options.KEYWORDS:
    query += " where"
    for word in words:
        query += " " + item + " like \"%" + word + "%\""
        if count < len(words) - 1:
            query += " and"
        count += 1
    if options.DATE_START and options.DATE_END:
        if options.KEYWORDS or options.LOCATIONS:
            query += " and"
        query += " datetime between \"" + options.DATE_START + "\" and \"" + options.DATE_END + "\""
    #if options.DATE_END:
        #query += " and datetime before \"" + options.DATE_END + "\""
    query += ";"
    print query
    curs = conn.cursor()
    curs.execute(query)
    rows = curs.fetchall()
    for row in rows:
        print "Title: " + str(row[1])
        print "Description: " + str(row[2])
        print "Keywords: " + str(row[3])
        print "Author: " + str(row[4])
        print "Date: " + str(row[5])
        print "Primary location: " + str(row[7])
        print "Secondary location: " + str(row[8])
        print "Url: " + str(row[6]) + "\n"
    print str(len(rows)) + " articles found matching the query."

if __name__ == '__main__':
    (options, args) = parse_arguments()
    main(options)
