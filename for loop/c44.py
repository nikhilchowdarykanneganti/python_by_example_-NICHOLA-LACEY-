#Challenge44
'''Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.'''
v=int(input('Enter nof invites:\n'))
if v<10:
	for i in range(v):
		n=input('Enter name:\n')
		print(n,'is invited')
else:
	print('Too many')