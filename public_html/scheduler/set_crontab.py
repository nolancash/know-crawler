import sys
import crontab
from crontab import CronTab

CRAWLER_COMMAND = '/usr/bin/python ProcessDispatcher.py'

DAY_OF_WEEK = [ "Sunday", "Monday", "Tuesday", "Wednesday", 
	"Thursday", "Friday", "Saturday" ]

def printTimeSetting():
	tab = CronTab()
	crawler_jobs = tab.find_command(CRAWLER_COMMAND)
	if not crawler_jobs:
		print 'There is no crawler job scheduled.'
		return
	crawler_job = crawler_jobs[0]
	minute = crawler_job.minute().value()
	hour = crawler_job.hour().value()
	dow = int(crawler_job.dow().value())
	print 'The crawler job is scheduled at ' + hour + ':' + minute + ' on ' + DAY_OF_WEEK[dow]

def setCronTab(hour, minute, days):
	tab = CronTab()
	
	# remove old crawler cron job(s)
	tab.remove_all(CRAWLER_COMMAND)
	
	cron = tab.new(command=CRAWLER_COMMAND)
	cron.minute().on(minute)
	cron.hour().on(hour)
	dsow = ','.join(map(str, days))
	cron.dow().on(dsow)
	
	tab.write()
	
def usage(prog_name):
	print "usage:\tpython " + prog_name
	print "\t--view-schedule\t(view crawler's schedule)"
	print "\t--edit-schedule\t(edit crawler's schedule)"
	
def getNumberInput(name, min_val, max_val):
	prompt_msg = name + ' (' + str(min_val) + ' - ' + str(max_val) + '): '
	while(True):
		var = raw_input(prompt_msg)
		if not var.isdigit():
			print 'invalid ' + name
			continue
		var = int(var)
		if var < min_val or var > max_val:
			print 'invalid ' + name
			continue
		return var
		
def getDaysInput():
	days = []
	print 'day(s) of week'
	prompt_msg = 'day (-1 to exit): '
	while(True):
		var = raw_input(prompt_msg)
		if var == '-1' and not days:
			print 'enter at least 1 day of week'
			continue
		if var == '-1':
			return days
		day = var[:3].lower()
		if day not in crontab.WEEK_ENUM:
			print 'invalid day of week'
			continue
		days.append(crontab.WEEK_ENUM.index(day))

def main():
	if len(sys.argv) != 2:
		usage(sys.argv[0])
		return
		
	option = sys.argv[1]
	if option == '--view-schedule':
		printTimeSetting()
	elif option == '--edit-schedule':
		hour = getNumberInput('hour', 0, 23)
		minute = getNumberInput('minute', 0, 59)
		days = getDaysInput()
		setCronTab(hour, minute, days)
	else:
		usage(sys.argv[0])

if __name__ == "__main__":
	main()
	