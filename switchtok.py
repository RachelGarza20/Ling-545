#I need to import the library for my script to utilize
import sys

#I want the program to read the corpus one line at a time and I need to define the variable of "last was english" as None because we cannot assume that any given corpus will begin in english. The variable switchpoints is the first variable that I will be counting. It will increment every time the corpuse switches from english to spanish or spanish to english. The variable counter will increment por token (where each token is a possible switchpoint) and reprsents "n" in the equation.

line = sys.stdin.readline()
last_was_eng = None
switchpoints = 0
counter = 0

#this function tells the program that the language of a token is english if the last column of a string ends in "eng", where languagestring is each token/word and its columns (from the tiktok.txt file)
def isenglish(languagestring):
        return languagestring.split('=')[-1] == 'eng'

#this function sets up the script to not count excess lines resulting from contractions like "can't" or "del". It tells the script to skip line when the line number of the token contains a hyphen (that only happens whent the token is a contraction). The len() function returns the number of items in the variable, if the variable split_line_number (which is line numbers with hyphens in them) does not have two numbers/characters, then return zero (basically, don't do the next command)  
def getskiplines(line_number):
	split_line_number = line_number.split('-')
	if len(split_line_number) != 2:
		return 0

#this command tells the script that if a line number does contain hyphen, to not count the lines that come after. In other words, I've told the script to only count contractions as one token for the purpose of the equation. It does this by taking the last number minus the first number and adding one,and this command line is not being touched unless there is a contraction (in otherwords, len(split_line_number) = 2). 
	return int(split_line_number[-1]) - int(split_line_number[0]) + 1

#this while loop, with its embedded for loop, do the main work of the script. the first few lines of the while loop tell the script to ignore any excess white space that it may encounter. 
while line:
	line = line.strip()
	if line == '':
		line = sys.stdin.readline()
		continue

#here, I define three variables. I split each line by white space to get my columns using the function line.split(). I then define the variable line_number, which is found in the first column. This will help the system to count the total number of tokens within the variable "counter".I also define the variable language, which I tell the system is found in the final column of each string (where I code for lang=eng or lang=span within the corpus). 	
	
	columns = line.split()
	line_number = columns[0]
	language = columns[-1]

#this first line tells the program to analyze only the lines that do not have punctuation (where language would be '_') and that do not begin in # (every segmented line of the corpuse begins wiht # and should not be counted)	
#the if state, sets last_was_eng to None, meaning false. This sets the script up to count switchpoints each time that the variable, language, switches from True (last_was_eng) to false (last_was_english!) and vice versa. 

	if language != '_' and line_number != '#':
		if last_was_eng is None:
			last_was_eng = isenglish(language)
		
		if last_was_eng != isenglish(language):
			switchpoints = switchpoints + 1

#this for statement tells the script to ignore excess lines resulting from contractions when counting, in other words, if i is 25 and the script encounters a getskiplines variable (defined as a line_number with a '-'), then it should skip redundant lines and read in the next token, as defined in the function above.
		for i in range(getskiplines(line_number)):
			sys.stdin.readline()

		last_was_eng = isenglish(language)		

#this says to increment the counter by one every time that a token is analyzed (and not skipped by the program for being white space or punctuation)		
		counter = counter + 1

#this tells the system to read in the next line
	line = sys.stdin.readline()

#the first two print statements helped me to double check that the script was counting switchpoints and tokens the way I wanted (which was helpful when I did some test runs with this script). The last print statement does the work of the I-index. Essentially, the total number of switchpoints is divided by the number of total tokens n, - 1. 	
print(switchpoints)
print(counter)
print(switchpoints/(counter - 1))
