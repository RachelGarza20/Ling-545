#
import sys, re

abbr = ['etc.', 'e.g.', 'i.e.', 'D.']

line = sys.stdin.readline()
increment = 1
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
	for token in line.split(' '):
		if token  == '':
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
	line = sys.stdin.readline() 
	print()

