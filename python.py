#!/usr/bin/python2.7

''' Python Notes

Quick and light language
	(small task/ automation.. works really well.. it's frictionless!)
	scripting language (Perl, Bash, JavaScript)

Quick turnaround (no compile!)

Very appropriate for small automation

Interpreted language

No compile-time type (dynamically typed)

python has a garbage collector

dir(sys) - lists all the things in a module 
help(sys) - 
	help(sys.argv) - 

Everything is done at runtime
	Python only checks a line when it hits that line

Strings are immutable!! (strings don't get changed)

Format Strings (like C)
	%s, %d (placeholders)
	'Hi %s, I have %d donuts' % ('Alice', 42)

	.lower() => lowercase
	.upper() => uppercase
	.find('a') => finds first occurrence and return
	strings not unicode strings
	a[x:y] => start at index x to index y (not including y)
		if either is omitted, start at beginning or end, repsectively
		negative indices, -1 very right, and decrements as you go left
	.startswith(str, beg=0, end=len(strength))
	.split('x') => returns a list splitted by 'x' (optional, else whitespace)

Lists.. 
	pointers when assigning variables to each other
	to copy:
		b = a[:]
	.append() => returns None, modifies list in place
	.pop(x) => pops the xth element, and modifies the list
del => deletes a, can also del a[1]
	sorted()
	':'.join(a)
	a.split(':')
	.extend(b) => b is a list, for each element in b, append to a 

range(x) => a list of numbers from 0 - x-1
	range(x,y) => start, stop
	range(x,y,z) => start, stop, step

Tuples = immutable, fixed size

Dictionaries (Dicts)/ Hashtables
	d.get('x') => returns None if DNE, or returns the value
	'a' in d => returns true or false if the key is in d
	d.keys() => returns a list of keys (random order)
	d.values() => returns a list of values (random order)
	d.items() => returns a list of tuples sized 2

f = open(filename, 'rU') => reads line by line
	"U" fixes the DOS endings and such
	f.close()
	f.readlines() => reads the whole file into a list, one line per element
	f.read() => reads entire file into one string
	f.write(text)

random.choice(list) => random element from the list

module os
	os.listdir(dir) => returns a list of files in that directory
	path = os.path.join(dir, filename) => path to the file
	os.path.abspath(path) => absolute path
	os.path.exists(path) => returns true if the path exists
	os.path.isfile(path) => returns true if path is a file
	os.path.isdir(path) => returns true if path is a directory
	os.mkdir() => makes a directory
	os.path.getmtime(path) => returns file modified time
	os.path.getatime(path) => returns file last access time
	os.path.getctime(path) => returns system's ctime (unix = last change)
	os.path.getsize(path) => return size of file in bytes

module shutil
	(source-path, dest-path) 

module commands

module calendar
	c = calendar.TextCalendar([firstweekday]), returns a plain text calendar 
	calendar.day_name => returns a list of days of the week in the current locale
	calendar.month_name => returns a list of months of the year in the current locale
	calendar.monthcalendar(year, month) => returns a matrix representing a month's calendar
	c.formatmonth(year, month, width, line)
	c.itermonthdays(year, month), return an output of each day in the month

module time
	time.ctime()

other functions
	filter(comparison, list) => returns a list filtered by things that equal the comparison 
	map(function, list) => returns a list of each element from the list ran through the function

packages = make your own modules
	__init__.py needed

'''

# Import modules
# commandline arguments, exit program
import sys

def main():
	print fib(int(sys.argv[1]))
	# Cat(sys.argv[1])
	# doSomething()
	# if len(sys.argv) > 1:
	# 	name = sys.argv[1]
	# else:
	# 	name = "NO NAME!"
	# Hello(name)
	# print mySlice("hello", 1, 4)

def Cat(filename):
	f = open(filename, 'rU')
	for line in f:
		print line, #trailing ',' prevents extra newlines
	f.close 

def doSomething():
	test = ['a', 'b', 'c', 'd']
	# for a in test:
		# print a

def Hello(name):
	if name == 'Jon' or name == 'Nick':
		print 'Woah, it\'s Jon time!'
		name += "???"
	else:
		print 'You\'re not special'
	name = name + '!!!!'
	print 'Hello', name


def mySlice(string, start, end):
	return string[start:end]

def fib(index):
	if index == 0 or index == 1:
		return index
	else:
		return fib(index - 2) + fib(index - 1)






# Standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()