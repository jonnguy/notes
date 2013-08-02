#!/usr/bin/env python

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt

filters = ['error', 'failure', 'fail']

a = {'01-06-13': {'fail': 0, 'failure': 0, 'error': 2}, '11-08-12': {'fail': 0, 'failure': 0, 'error': 773}, '01-03-13': {'fail': 0, 'failure': 0, 'error': 2}, '05-30-13': {'fail': 0, 'failure': 0, 'error': 519}, '07-30-13': {'fail': 0, 'failure': 0, 'error': 3}, '11-07-12': {'fail': 0, 'failure': 0, 'error': 255}, '01-19-13': {'fail': 0, 'failure': 0, 'error': 2}, '01-07-13': {'fail': 0, 'failure': 0, 'error': 3}, '04-26-13': {'fail': 0, 'failure': 0, 'error': 2}, '10-28-12': {'fail': 0, 'failure': 0, 'error': 777}, '05-07-13': {'fail': 0, 'failure': 0, 'error': 258}, '02-04-13': {'fail': 0, 'failure': 0, 'error': 258}, '08-01-13': {'fail': 53, 'failure': 0, 'error': 14}, '03-09-13': {'fail': 0, 'failure': 0, 'error': 2}, '01-12-13': {'fail': 0, 'failure': 0, 'error': 2}, '05-13-13': {'fail': 0, 'failure': 0, 'error': 2}, '12-04-12': {'fail': 0, 'failure': 0, 'error': 2}, '06-18-13': {'fail': 0, 'failure': 0, 'error': 3}, '07-07-13': {'fail': 0, 'failure': 0, 'error': 3}, '11-05-12': {'fail': 0, 'failure': 0, 'error': 1543}, '12-18-12': {'fail': 0, 'failure': 0, 'error': 2}, '04-28-13': {'fail': 0, 'failure': 0, 'error': 1}, '06-07-13': {'fail': 0, 'failure': 0, 'error': 1}, '02-12-13': {'fail': 0, 'failure': 0, 'error': 255}, '12-15-12': {'fail': 0, 'failure': 0, 'error': 4}, '03-30-13': {'fail': 0, 'failure': 0, 'error': 1}, '10-27-12': {'fail': 0, 'failure': 0, 'error': 4}, '05-03-13': {'fail': 0, 'failure': 0, 'error': 2}, '01-20-13': {'fail': 0, 'failure': 0, 'error': 2}, '02-19-13': {'fail': 0, 'failure': 0, 'error': 2}, '10-31-12': {'fail': 0, 'failure': 0, 'error': 2}, '03-05-13': {'fail': 0, 'failure': 0, 'error': 2}, '11-02-12': {'fail': 0, 'failure': 0, 'error': 4}, '02-14-13': {'fail': 0, 'failure': 0, 'error': 513}, '12-02-12': {'fail': 0, 'failure': 0, 'error': 1026}, '06-21-13': {'fail': 0, 'failure': 0, 'error': 3}, '03-24-13': {'fail': 0, 'failure': 0, 'error': 2}, '06-06-13': {'fail': 0, 'failure': 0, 'error': 1}, '12-29-12': {'fail': 0, 'failure': 0, 'error': 4}, '05-01-13': {'fail': 0, 'failure': 0, 'error': 2}, '05-05-13': {'fail': 0, 'failure': 0, 'error': 515}, '06-09-13': {'fail': 0, 'failure': 0, 'error': 3}, '03-29-13': {'fail': 0, 'failure': 0, 'error': 2}, '04-23-13': {'fail': 0, 'failure': 0, 'error': 2}, '11-06-12': {'fail': 0, 'failure': 0, 'error': 513}, '02-09-13': {'fail': 0, 'failure': 0, 'error': 255}, '06-20-13': {'fail': 0, 'failure': 0, 'error': 3}, '03-13-13': {'fail': 0, 'failure': 0, 'error': 2}, '12-07-12': {'fail': 0, 'failure': 0, 'error': 2}, '06-10-13': {'fail': 0, 'failure': 0, 'error': 1}, '02-16-13': {'fail': 0, 'failure': 0, 'error': 777}, '07-29-13': {'fail': 0, 'failure': 0, 'error': 1539}, '07-05-13': {'fail': 0, 'failure': 0, 'error': 3}, '04-22-13': {'fail': 0, 'failure': 0, 'error': 2}, '06-12-13': {'fail': 0, 'failure': 0, 'error': 514}, '02-18-13': {'fail': 0, 'failure': 0, 'error': 2}, '07-01-13': {'fail': 0, 'failure': 0, 'error': 513}, '01-31-13': {'fail': 0, 'failure': 0, 'error': 2}, '02-24-13': {'fail': 0, 'failure': 0, 'error': 2}, '06-13-13': {'fail': 0, 'failure': 0, 'error': 1}, '11-25-12': {'fail': 0, 'failure': 0, 'error': 2}, '02-11-13': {'fail': 0, 'failure': 0, 'error': 258}, '12-12-12': {'fail': 0, 'failure': 0, 'error': 2}, '06-11-13': {'fail': 0, 'failure': 0, 'error': 1}, '04-11-13': {'fail': 0, 'failure': 0, 'error': 2}, '12-24-12': {'fail': 0, 'failure': 0, 'error': 2}, '03-25-13': {'fail': 0, 'failure': 0, 'error': 1}, '11-26-12': {'fail': 0, 'failure': 0, 'error': 515}, '11-12-12': {'fail': 0, 'failure': 0, 'error': 257}, '05-28-13': {'fail': 0, 'failure': 0, 'error': 334}, '12-11-12': {'fail': 0, 'failure': 0, 'error': 2}, '12-01-12': {'fail': 0, 'failure': 0, 'error': 2}, '07-09-13': {'fail': 0, 'failure': 0, 'error': 4}, '06-16-13': {'fail': 0, 'failure': 0, 'error': 2}, '03-16-13': {'fail': 0, 'failure': 0, 'error': 3}, '04-15-13': {'fail': 0, 'failure': 0, 'error': 258}, '02-07-13': {'fail': 0, 'failure': 0, 'error': 258}, '05-29-13': {'fail': 0, 'failure': 0, 'error': 290}, '04-03-13': {'fail': 0, 'failure': 0, 'error': 2}, '03-28-13': {'fail': 0, 'failure': 0, 'error': 2}, '10-29-12': {'fail': 0, 'failure': 0, 'error': 4}, '04-16-13': {'fail': 0, 'failure': 0, 'error': 257}, '03-23-13': {'fail': 0, 'failure': 0, 'error': 2}, '03-21-13': {'fail': 0, 'failure': 0, 'error': 1}, '11-22-12': {'fail': 0, 'failure': 0, 'error': 2}, '06-30-13': {'fail': 0, 'failure': 0, 'error': 516}, '12-23-12': {'fail': 0, 'failure': 0, 'error': 2}, '11-10-12': {'fail': 0, 'failure': 0, 'error': 513}, '02-05-13': {'fail': 0, 'failure': 0, 'error': 513}, '05-20-13': {'fail': 0, 'failure': 0, 'error': 1}, '07-16-13': {'fail': 0, 'failure': 0, 'error': 3}, '11-04-12': {'fail': 0, 'failure': 0, 'error': 258}, '12-27-12': {'fail': 0, 'failure': 0, 'error': 2}, '11-09-12': {'fail': 0, 'failure': 0, 'error': 513}, '10-26-12': {'fail': 0, 'failure': 0, 'error': 8}, '03-31-13': {'fail': 0, 'failure': 0, 'error': 4}, '07-06-13': {'fail': 0, 'failure': 0, 'error': 6}, '05-02-13': {'fail': 0, 'failure': 0, 'error': 2}, '07-28-13': {'fail': 0, 'failure': 0, 'error': 513}, '04-01-13': {'fail': 0, 'failure': 0, 'error': 6}, '01-02-13': {'fail': 0, 'failure': 0, 'error': 2}, '03-19-13': {'fail': 0, 'failure': 0, 'error': 2}, '07-31-13': {'fail': 0, 'failure': 0, 'error': 258}, '01-29-13': {'fail': 0, 'failure': 0, 'error': 2}, '04-02-13': {'fail': 0, 'failure': 0, 'error': 2}, '01-26-13': {'fail': 0, 'failure': 0, 'error': 2}, '10-25-12': {'fail': 0, 'failure': 0, 'error': 7}, '11-01-12': {'fail': 0, 'failure': 0, 'error': 4}, '03-22-13': {'fail': 0, 'failure': 0, 'error': 1}, '05-31-13': {'fail': 0, 'failure': 0, 'error': 2}, '04-30-13': {'fail': 0, 'failure': 0, 'error': 2}, '06-17-13': {'fail': 0, 'failure': 0, 'error': 32}, '05-06-13': {'fail': 0, 'failure': 0, 'error': 261}, '02-06-13': {'fail': 0, 'failure': 0, 'error': 1030}}

dates = a.keys()

x = [dt.datetime.strptime(d, '%m-%d-%y').date() for d in dates]
y = []
for date in a.keys():
	y.append(a[date]['error'])


print y
print len(y), len(x)

ax = plt.subplot(111)
ax.bar(x, y, width=5, color='r')
ax.xaxis_date()

y = []
for date in a.keys():
	y.append(a[date]['fail'])

b = plt.subplot(111)
b.bar(x,y, width=5, color='b')
b.xaxis_date()

y = []
for date in a.keys():
	y.append(a[date]['failure'])

print y

b = plt.subplot(111)
b.bar(x,y, width=5, color='g')
b.xaxis_date()



plt.show()