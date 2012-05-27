import MySQLdb
from crontab import CronTab

CRAWLER_COMMAND = '/usr/bin/python ProcessDispatcher.py'

class Scheduler:
	def __init__(self):
		self.conn = MySQLdb.connect(host = "ovid.u.washington.edu",
																user = "root",
																passwd = "purple pony disco",
																db = "know_db",
																port = 32001)
																
	def querySchedule(self):
		curs = self.conn.cursor()
		query = "select * from schedule;"
		curs.execute(query)
		rows = curs.fetchall()
		
		if rows:
			hour = rows[0][1]
			days = []
			
			for row in rows:
				day = row[0]
				days.append(day)
				
			return hour, days
		
		# default schedule: 3 am daily
		return 3, []
			
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
	