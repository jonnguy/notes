#!/usr/bin/python2.7

# 1st argument will be the directory of where to read logs from

import sys
import os
import re

# For each file, find the stuff with a regular expression
def parseLogs(files):
	alllines = ""
	for file in files:
		if os.path.isfile(file):
			f = open(file, 'rU')
			for line in f:
				match = re.search(r'((GET|POST).* 404 .*)|.*error.*', line)
				if match:
					alllines += match.group() + "\n"
					# print match.group()
			f.close()
	count = alllines.count("\n")

	print "Found", count, "instances."
	return alllines

def savelinestofile(lines):
	filename = "log_filtered"
	f = open(filename, 'w')
	f.write(lines)
	print "Successfully wrote to", filename
	f.close()
	return


# Create a list of files in the directory, ignoring hidden files and directories 
# and files with extensions
def readFilesFromDir(dir, recursively=False):
	if not os.path.exists(dir):
		return "The directory doesn't exist"
	files = os.listdir(dir)
	new_files = []


	for dirpath, directories, files in os.walk(dir):
		print str(dirpath) + " " + str(directories) + " " + str(files) + "\n"

	if recursively:
		for dirpath, dirs, files in os.walk(dir):
			for file in files:
				path = os.path.join(dirpath, file)
				if not os.path.isdir(path) and file[0] != ".":
					match = re.search(r"log", file)
					# match = re.search(r"\.[a-zA-Z]+", file)
					if match and "log" in match.group():
						new_files.append(path)

	# create a new list with non-directories and non-hidden
	else:
		for file in files:
			path = os.path.join(dir, file)
			if not os.path.isdir(path) and file[0] != ".":
				# match = re.search(r"\.[a-zA-Z]+", file)
				match = re.search(r"log", file)
				if match and "log" in match.group():
					new_files.append(path)


	# print "Other directories to read:"
	# for direc in moredirs:
	# 	print "  " + direc

	print "Reading the following files: "
	for file in new_files:
		print "  " + os.path.abspath(file)


	return new_files

def usage():
	print """ Usage: %s [options] [directory to read]
		-h, --help			display help
		-v, --verbose		display verbose 
		-r 					recrusively go through directories
	""" % sys.argv[0]

	sys.exit()

def main():
	import getopt
	global VERBOSE_TAG
	recurs = False

	options, args = getopt.getopt(sys.argv[1:], "rhv", ["help", "verbose"])

	for option, arg in options:
		if option in ("-h", "--help"):
			usage()
		elif option in ("-v", "--verbose"):
			VERBOSE_TAG = True
		elif option == "-r":
			recurs = True

	dir = sys.argv[-1]
	print dir

	# If there are 0 arguments, return
	# if len(args) != 2:
	# 	print 'usage: ./grablogs.py [-r] [--help, --verbose] directory_to_logs'
	# 	sys.exit(1)

	# dir = args[1]

	files = readFilesFromDir(dir, recurs)
	# print readFilesFromDir(dir)

	allmatches = parseLogs(files)
	savelinestofile(allmatches)

	return

if __name__ == "__main__":
	main()
