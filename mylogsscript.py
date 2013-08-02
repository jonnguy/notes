#!/usr/bin/python

import sys, os, re
import datetime

VERBOSE_TAG = False

"""
This program grabs the log files and looks for lines with "error" in it with a date.
	We'll use matplotlib to display a histogram of errors based on the date.

"""

# Prints out usage text
def usage(error = None):

	if error:
		print "Error: ", error

	print """ Usage ./mylogsscript.py [options] [directory]
   -v, --verbose	verbose output
   -h, --help		display help
   -r, -R 		recursively go through directory
   -a 			read all files, not just "log" (not including hidden)
   -A 			read all files, including those that begin with '.' (overwrites 'a')
   -f filter 		filter by keyword 'filter', default is 'error'
	"""

# Returns (options, dir)
def getArgs():
	import getopt
	global VERBOSE_TAG

	opts = {}

	options, args = getopt.getopt(sys.argv[1:], "hvraAo:", ["help", "verbose"])

	for option, optarg in options:
		if option in ("-h", "--help"):
			usage()
		elif option == "-r":
			opts['recurse'] = True
			# recurse = True
		elif option == "-a":
			opts['all_files_not_hidden'] = True
		elif option == "-A":
			opts['all_files'] = True
		elif option == "-o":
			opts['output'] = optarg
		elif option == "-v":
			VERBOSE_TAG = True

	return opts, args

# Returns a list of all absolute paths to files
def getAllFiles(dirs, opts):
	files_to_read = [] # absolute path to the files

	for dir in dirs:
		if os.path.exists(dir):
			if VERBOSE_TAG:
				print "Reading from:", dir
				if opts.get('recurse'):
					print "Also reading from directories: "

			# Search through directory
			paths = os.listdir(dir)

			for path in paths:
				path = os.path.join(dir, path)

				# Read through directories if the tag is on
				if os.path.isdir(path):
					if opts.get('recurse'):
						for dirpath, dirname, files in os.walk(path):
							print "  ", dirpath
							for file in files:
								files_to_read.append(os.path.join(dirpath,file))
				else: #it's not a path
					files_to_read.append(path)

		else:
			print "** Error:", dir, "is NOT a valid path. It has been ignored."

	# Filter out if it's only logs (-a, -A are not specified)
	if not opts.get('all_files') and not opts.get('all_files_not_hidden'):
		for file in files_to_read[:]:
			filename = os.path.basename(file)

			# I guess we don't have to really do a regex here.
			# match = re.search(r'^((?!log).)*$', filename)
			match = "log" in filename
			if match: 
				files_to_read.remove(file)
			# files_to_read.remove(file)

	# Filter out hidden if -A is not specified
	if opts.get('all_files_not_hidden') and not opts.get('all_files'):
		for file in files_to_read[:]:
			filename = os.path.basename(file)
			if filename.startswith('.'):
				files_to_read.remove(file)

	# for file in files_to_read:
	# 	print file

	return files_to_read

# This will parse the files and return a dictionary as: dict[date][filter] = count
def filter_and_count (filepaths, opts):
	filter_by = ['error', 'fail', 'failure']
	date_dict = {}

	# my regex for date in the format, where x are letters and n are numbers:
	# 	nn/nn/nn, n/nn/nn,
	# 	mmmm dd , m is month letter
	# EDIT: dates get really messy.. especially the ones that are spelled out
	# 	some don't even have the year..
	filter_expression = "|".join(filter_by)

	regexstr = r'(?P<date>(\d?\d[-\/ ]{1}(\d?\d|[a-zA-Z]{3,4})[-\/ ]{1}\d?\d{2,4})|([a-zA-Z]{3,4} +\d?\d)).*(?i)(?P<filter>'+filter_expression+').*'
	print "Regexstr:", regexstr
	reg = re.compile(regexstr)

	# Use user's filter function
	if opts.get('filter_by'):
		filter_by = opts['filter_by']

	# Read each file
	total_counts = 0
	for file in filepaths:
		single_count = 0

		if not os.path.isfile(file):
			print "Error opening", file
		else: 
			if VERBOSE_TAG:
				print "Starting to parse", file

			read = open(file, 'rU')
			for line in read:
				match = reg.search(line) # search and ignore case
				if match:
					# print "    Found: ", match.group()
					date = match.group('date')
					filter = match.group('filter').lower()

					# replace / and ' ' with -, to make dates uniform, kind of
					date = re.sub('[\/ ]+','-', date)

					current_year = str(datetime.datetime.now().year)[-2:] # last 2 digits
					format = '%y-%m-%d' if date.startswith(current_year) else '%m-%d-%y'

					# now for the funky MMMM-dd ones..
					if date[:3].isalpha():
						date += "-"+current_year
						format = "%b-%d-%y"

					# makes all the dates uniform in the form mm-dd-yy
					dateobj = datetime.datetime.strptime(date, format)
					new_date = dateobj.strftime("%m-%d-%y")

					# print "\t filter type:", filter

					# if the date is already in there, add
					if date_dict.get(new_date):
						# Check if the type is already in
						if date_dict[new_date].get(filter):
							date_dict[new_date][filter] += 1
						else:
							date_dict[new_date][filter] = 1
					else:
						date_dict[new_date] = {}
						date_dict[new_date][filter] = 1

					single_count+= 1

		if VERBOSE_TAG:
			print "  Found", single_count, "lines in", file
		total_counts += single_count

	if VERBOSE_TAG:
		print "keys:", len(date_dict.keys())
		print "** Found", total_counts, "lines in all files **"

	# print date_dict

	return date_dict

def main():
	# Get the arguments
	options, dirs = getArgs()

	# print options, dirs

	files_to_read = getAllFiles(dirs, options)

	# gets a dictionary in the form date_dict[date][filter] = count
	date_dict = filter_and_count(files_to_read, options)

if __name__ == "__main__":
	main()
