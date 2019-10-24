#Challenge39
'''Ask the user to enter a number between 1
and 12 and then display the times table for
that number.'''
num=int(input('Enter no:\n'))
for i in range(1,11):
	print('{0}x{1}={2}'.format(num,i,num*i))