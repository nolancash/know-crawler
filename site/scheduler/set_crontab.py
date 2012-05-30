import sys
import crontab
from crontab import CronTab
from scheduler import Scheduler

DAYS_OF_WEEK = [ "Sunday", "Monday", "Tuesday", "Wednesday", 
	"Thursday", "Friday", "Saturday" ]

def printTimeSetting():
	tab = CronTab()
	crawler_jobs = tab.find_command(scheduler.CRAWLER_COMMAND)
	if not crawler_jobs:
		print 'There is no crawler job scheduled.'
		return
	crawler_job = crawler_jobs[0]
	minute = crawler_job.minute().value()
	if len(minute) < 2:
		minute = '0' + minute
	hour = crawler_job.hour().value()
	dsow = crawler_job.dow().value().split(',')
	days = ', '.join(map(lambda x : DAYS_OF_WEEK[int(x)], dsow))
	print 'The crawler job is scheduled at ' + hour + ':' + minute + " o'clock on " + days + '.'
	
def usage(prog_name):
	print "usage:\tpython " + prog_name
	print "\t--view-schedule\t(view crawler's schedule)"
	print "\t--edit-schedule\t(edit crawler's schedule)"
	
def getNumberInput(name, min_val, max_val):
	prompt_msg = name + ' (' + str(min_val) + ' - ' + str(max_val) + '): '
	while(True):
		var = raw_input(prompt_msg)
		if not var.isdigit():
			print 'invalid ' + name + ': not a digit'
			continue
		var = int(var)
		if var < min_val or var > max_val:
			print 'invalid ' + name + ': out of range'
			continue
		return var
		
def getDaysInput():
	days = []
	print 'day(s) of week'
	prompt_msg = 'day (-1 to finish): '
	while(True):
		var = raw_input(prompt_msg)
		if var == '-1' and not days:
			print 'enter at least 1 day of week'
			continue
		if var == '-1':
			return sorted(days)
		day_enum = var[:3].lower()
		if day_enum not in crontab.WEEK_ENUM:
			print 'invalid day of week'
			continue
		day = crontab.WEEK_ENUM.index(day_enum)
		if day in days:
			print var + ' is alreay entered'
			continue
		days.append(day)

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
		scheduler = Scheduler()
		scheduler.setCronTab(hour, minute, days)
		printTimeSetting()
	else:
		usage(sys.argv[0])

if __name__ == "__main__":
	main()
	