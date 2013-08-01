#!/usr/bin/python2.7

import calendar
import sys
import os 
import time
import datetime
import shutil #copy, archive
from zipfile import ZipFile
import urllib # url stuff
import json #json stuff

args = sys.argv

# c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2013, 1, 0, 0)
# print str

# # hc = calendar.HTMLCalendar(calendar.SUNDAY)
# # hstr = hc.formatmonth(2013, 1)
# # print hstr

# for d in calendar.day_name:
# 	print d

# for m in calendar.month_name:
# 	print m

# print calendar.monthcalendar(2013, 2)

# for m in range(1,13):
# 	cal = calendar.monthcalendar(2013, m)
# 	weekone = cal[0]
# 	weektwo = cal[1]
# 	# print weekone + weektwo

# 	if weekone[calendar.FRIDAY] != 0:
# 		meetday = weekone[calendar.FRIDAY]
# 	else:
# 		meetday = weektwo[calendar.FRIDAY]

# 	# print "%10s %2d" % (calendar.month_name[m], meetday)

print 'args:', args

print 'args[1]:', args[1]
print 'abspath:', str(os.path.abspath(args[1]))
print 'realpath:', str(os.path.realpath(args[1]))
print 'dirname:', os.path.dirname(os.path.realpath(args[1]))
print 'exists:', str(os.path.exists(args[1]))
print 'isfile:', str(os.path.isfile(args[1]))
print 'isdir:', str(os.path.isdir(args[1]))
print 'ctime:', time.ctime(os.path.getmtime(args[1]))
print 'datetime:', datetime.datetime.fromtimestamp(os.path.getmtime(args[1]))

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(args[1]))
print "It has been " + str(td) + " since the file was modified."
print "or, " + str(round(td.total_seconds(), 2)) + " seconds."

src = os.path.abspath(args[1])
dest = src + ".bak"
shutil.copy(src,dest)
shutil.copystat(src,dest)
os.rename(args[1], args[1])

# root_dir = os.path.dirname(os.path.abspath(args[1]))
# shutil.make_archive("archive", "zip", root_dir)

# with ZipFile("testzip.zip", "w") as newzip:
# 	newzip.write(args[1])
# 	newzip.write(args[1]+".bak")
def printResults(data):
	# Use the json module to load the string data into a dictionary
	theJSON = json.loads(data)

	# now we can access the contents of the JSON like any other Python object
	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]

	# output the number of events, plus the magnitude and each event name  
	count = theJSON["metadata"]["count"];
	print str(count) + " events recorded"

	# for each event, print the place where it occurred
	for i in theJSON["features"]:
		print i["properties"]["place"]

	# print the events that only have a magnitude greater than 4
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

	# print only the events where at least 1 person reported feeling something
	print "Events that were felt:"
	for i in theJSON["features"]:
		feltReports = i["properties"]["felt"]
		if (feltReports != None) & (feltReports > 0):
		    print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
weburl = urllib.urlopen(url)
print weburl.getcode()
if (weburl.getcode() == 200):
	data = weburl.read()
	printResults(data)
else:
	print "Received an error from the server, cannot retrieve results " + weburl.getcode()


if 1+1==3:
	a = 'Hello'
else:
	b = 'World'
print a
