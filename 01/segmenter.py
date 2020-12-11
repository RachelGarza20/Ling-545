import sys

#this first line asks the program to read in one line at a time and the second  constrains what a line is and when it stops
line = sys.stdin.readline()
while line != '':
	#this next line tells what to look for and what to replace it with
	for c in '.':
		line = line.replace(c, c + '\n')
	#this line defines what the output should be
	sys.stdout.write(line)
	#this asks the program to continue to the next line
	line = sys.stdin.readline()
