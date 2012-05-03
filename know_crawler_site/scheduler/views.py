# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

from crontab import CronTab

def scheduler(request):
	if request.method == 'POST':
		hour = request.POST['hour']
		minute = request.POST['minute']
		period = request.POST['period']
		
		am = period == 'am'
		
		if !am and hour != 12:
			hour += 12
		elif am and hour == 12:
			hour = 0
			
		setCronTab(hour, minute)
		
		message = "Crawling time is set to " + hour + ":" + minute + " " + period + "."
		return render_to_response('index.html', { "message" : message })
		
	return HttpResponse('Schedule is not submitted.')

"""
*     *     *     *     *  command to be executed
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- day of week (0 - 6) (Sunday=0)
|     |     |     +------- month (1 - 12)
|     |     +--------- day of month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
"""

CRAWLER_COMMAND = 'crawler.py'

def setCronTab(hour, minute):
	tab = CronTab()
	
	# remove old crawler cron job(s)
	tab.remove_all(CRAWLER_COMMAND)
	
	cron = tab.new(command=CRAWLER_COMMAND)
	cron.minute().on(minute)
	cron.hour().on(hour)
	
	tab.write()
