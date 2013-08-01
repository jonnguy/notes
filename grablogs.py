#!/usr/bin/python2.7

# 1st argument will be the directory of where to read logs from

import sys
import os
import re

# For each file, find the stuff with a regular expression
def parseLogs(files):
	alllines = ""
	for file in files:
		f = open(file, 'rU')
		for line in f:
			match = re.search(r'(?P<get>(GET|POST).*404.*)|(?P<err>.*error.*)', line)
			if match:
				# print match.group()
				if match.group('err'):
					print "Err:", str(match.group('err'))
				else:
					print "GET/POST:", str(match.group('get'))
				# print match.group('err')
				# print match.start()
				# print match.end()
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
def readFilesFromDir(dir):
	if not os.path.exists(dir):
		return "The directory doesn't exist"
	files = os.listdir(dir)

	# create a new list with non-directories and non-hidden
	new_files = []
	for file in files:
		path = os.path.join(dir, file)
		if not os.path.isdir(path) and file[0] != ".":
			match = re.search(r"\.[a-zA-Z]+", file)
			if not match or match.group() == ".log":
				new_files.append(os.path.join(dir,file))

	return new_files

def main():
	args = sys.argv

	# If there are 0 arguments, return
	if len(args) != 2:
		print 'usage: ./grablogs.py directory_to_logs'
		sys.exit(1)

	dir = args[1]

	files = readFilesFromDir(dir)
	print readFilesFromDir(dir)

	allmatches = parseLogs(files)
	savelinestofile(allmatches)

	return

if __name__ == "__main__":
	main()
