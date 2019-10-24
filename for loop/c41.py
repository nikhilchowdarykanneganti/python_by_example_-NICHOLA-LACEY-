#Challenge41
'''Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.'''
name =input('Enter name:\n')
n=int(input('Enter number:\n'))
if n<10:
	for i in range(n):
		print(name)
else:
	for i in range(3):
		print('Too high\n')