#Challenge46
'''Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program.'''
c=int(input('Enter number:\n'))
while c<5:
	c=int(input('Enter number:\n'))
print('last number you entered is',c)