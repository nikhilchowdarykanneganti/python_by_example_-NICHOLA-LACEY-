#Challenge38
'''Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.'''
name=input('Enter name:\n')
for i in range(int(input('Enter no:\n'))):
	for j in name:
		print(j)