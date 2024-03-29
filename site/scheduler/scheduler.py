"""
Scheduler handles KNOW-Crawler's time setting. It checks if the crawler is enabled. 
If so, queries the time setting from the database and schedules a cron job to run 
the crawler accordingly. Otherwise, it removes any existing crawler cron job.
"""

import MySQLdb
from crontab import CronTab

CRAWLER_COMMAND = "/rc12/d04/knowcse2/site/scheduler/run_crawler.sh"
DAY_COLUMN_INDEX = 0
HOUR_COLUMN_INDEX = 1

class Scheduler:
	def __init__(self):
		self.conn = MySQLdb.connect(host = "ovid01.u.washington.edu",
																user = "root",
																passwd = "purple pony disco",
																db = "know_db",
																port = 32002)
																
	"""
	Checks if the crawler is enabled.
	"""
	def queryCrawlerSwitch(self):
		curs = self.conn.cursor()
		query = "select * from crawler_switch;"
		curs.execute(query)
		rows = curs.fetchall()
		
		if not rows:
			raise Exception, "'crawler_switch' table is empty"
			
		state = rows[0][0];
		return state;			
	
	"""
	Queries and returns the crawl schedule as a tuple of (hour, days).
	"""
	def querySchedule(self):
		curs = self.conn.cursor()
		query = "select * from schedule;"
		curs.execute(query)
		rows = curs.fetchall()
		
		if not rows:
			raise Exception, "'schedule' table is empty"
		
		hour = rows[0][HOUR_COLUMN_INDEX]
		days = []
		
		for row in rows:
			day = row[DAY_COLUMN_INDEX]
			days.append(day)
			
		return hour, days
		
	"""
	Schedules a cron job to run the crawler.
	"""
	def setCronTab(self, hour, minute, days):
		tab = CronTab()
		
		# remove old crawler cron job(s)
		tab.remove_all(CRAWLER_COMMAND)
		
		cron = tab.new(command=CRAWLER_COMMAND)
		cron.minute().on(minute)
		cron.hour().on(hour)
		
		if days:
			dow = ",".join(map(str, days))
			cron.dow().on(dow)
		
		tab.write()
		
		
def main():
	scheduler = Scheduler()
	state = scheduler.queryCrawlerSwitch()
	
	if state:
		hour, days = scheduler.querySchedule()
		scheduler.setCronTab(hour, 0, days)
	else:
		tab = CronTab()
		# remove crawler cron job(s)
		tab.remove_all(CRAWLER_COMMAND)
		tab.write()

if __name__ == "__main__":
	main()
	