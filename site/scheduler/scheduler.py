# Scheduler handles KNOW-Crawler's time setting. It queries the time setting 
# from the database and schedules a cron job to run the crawler accordingly.

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
																
	def querySchedule(self):
		curs = self.conn.cursor()
		query = "select * from schedule;"
		curs.execute(query)
		rows = curs.fetchall()
		
		if rows:
			hour = rows[0][HOUR_COLUMN_INDEX]
			days = []
			
			for row in rows:
				day = row[DAY_COLUMN_INDEX]
				days.append(day)
				
			return hour, days
		
		# schedule table is empty: no time set
		return None
			
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
	hour, days = scheduler.querySchedule()
	scheduler.setCronTab(hour, 0, days)

if __name__ == "__main__":
	main()
	