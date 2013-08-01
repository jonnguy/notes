#!/usr/bin/python2.7

import calendar
import sys
import os 
import time
import datetime

args = sys.argv
print args

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

print args[1]
print str(os.path.exists(args[1]))
print str(os.path.isfile(args[1]))
print str(os.path.isdir(args[1]))
print time.ctime(os.path.getmtime(args[1]))