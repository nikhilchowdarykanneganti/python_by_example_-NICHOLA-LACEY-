#Challenge49
'''Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.'''
c=0
q=int(input('Enter a number:\n'))
while q!=50:
	if q<50:
		print('Too low\n')
		q=int(input('Enter a number:\n'))
	elif q>50:
		print('Too high\n')
		q=int(input('Enter a number:\n'))
	c+=1	
print('You took',c+1,'attemps.')



