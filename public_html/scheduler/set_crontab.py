import sys
from crontab import CronTab

CRAWLER_COMMAND = '/usr/bin/python ProcessDispatcher.py'

def setCronTab(hour, minute):
	tab = CronTab()
	
	# remove old crawler cron job(s)
	tab.remove_all(CRAWLER_COMMAND)
	
	cron = tab.new(command=CRAWLER_COMMAND)
	cron.minute().on(minute)
	cron.hour().on(hour)
	
	tab.write()

def main():
	hour = sys.argv[1]
	minute = sys.argv[2]
	setCronTab(hour, minute)

if __name__ == "__main__":
	main()
	