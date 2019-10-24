#Challenge50
'''Ask the user to enter a number between
10 and 20. If they enter a value under 10,
display the message “Too low” and ask
them to try again. If they enter a value
above 20, display the message “Too high”
and ask them to try again. Keep repeating
this until they enter a value that is
between 10 and 20 and then display the
message “Thank you”.'''
n=int(input('Enter number b/w 10 and 20'))
while 1:
	if n<10:
		print('Too low\n')
		n=int(input('Enter number b/w 10 and 20'))
	elif n>20:
		print('Too high\n')
		n=int(input('Enter number b/w 10 and 20'))
	else:
		print('Thank you!!!')
		break

