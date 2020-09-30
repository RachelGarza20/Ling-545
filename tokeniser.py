import sys, re

#I included the abbreviation D. for doctor here
abbr = ['etc.', 'e.g.', 'i.e.', 'D.']

def tokenise(line, abbr):
	#after seeing the output I included several more symbols below
	line = re.sub(r'([\(\)"?:!;*,])', r' \n', line)
	#I replaced \g<1> with \n to create new lines which seemed to work
	line = re.sub(r'([^0-9]),', r' \n', line)
	line = re.sub(r',([^0-9])',r', \n', line)
	line = re.sub(r'  +', ' ', line)
	#The line below is my attempt at replacing all ' ' with \n, this did not 	work, but I am not sure how else to clean up the output
	line = re.sub(r'(' '), r' \n', line)

	#I maintained what was discussed in the tokenisation lecture, when I tri	ed creating my own code without utilizing what was done in the lecture I 	had a more difficult time configuring something that seemed to further s	plit the text
	output = []
	for token in line.split(' '):
		if token == '':
			continue 
		if token [-1] == '.' and token not in abbr:
			token = token[:-1] + ' .'
		output.append(token)
	return ' '.join(output)

#this is necessary for the program to read by lines and output lines
line = sys.stdin.readline()
while line != '':
	print(tokenise(line.strip('\n'), abbr))
	line = sys.stdin.readline()
