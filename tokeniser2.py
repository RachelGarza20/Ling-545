#need to import the module for my script to use. sys and re give information for the script to use
import sys, re

#this defines what the abbreviations in my corpus are so that they will not be split from their punctuation later on
abbr = ['etc.', 'e.g.', 'i.e.', 'D.']

#this tells the system to read in one line at a time
line = sys.stdin.readline()
#this variable counts the number of sentences/segments
increment = 1

#this while loop and the if statement that it encompasses do the main work of tokenizing, it lists rules for what should be split and when. the print statements set up the sent_id and text lines that print out the full sentence before it is tokenised. The counter will increment for every token within a sentence (it will start over when a new sentence is tokenized). 
while line:
	line = line.strip()
	if line == '':	
		line = sys.stdin.readline()
		continue
	print('# sent_id =', increment)
	print('# text =',line)
	line = line.replace('[', '[ ')
	line = line.replace('(','( ')
	line = re.sub(r'([\[\]()"?:!;*])', r' \g<1>', line)
	line = re.sub(r'([^0-9]),', r' \g<1> ,', line)
	line = re.sub(r',([^0-9])',r', \g<1>', line)
	line = re.sub(r'  +', ' ', line)
	increment = increment + 1
	counter = 1

#this for loop formats the tokens into rows, with special attention to full stops, where it says to split the full stop into its own token if it is not in an abbreviation.
	for token in line.split(' '):
		if token == '':
			continue
		if token [-1] == '.' and token not in abbr:
			row = (counter, token [0:-1],'_','_','_','_','_','_','_','_')
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %row)
			counter = counter + 1
			row = (counter, token[-1],'_','_','_','_','_','_','_','_')
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %row)	
		else:
			row = (counter, token,'_','_','_','_','_','_','_','_')
			print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %row)
		counter = counter + 1
	
#this says to read in the next line
	line = sys.stdin.readline() 
	print()
