#Challenge43
'''Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.'''
c=input('Select direction (up/down):\n')
if c=='up':
	for i in range(1,int(input('Enter the top bound'))+1):
		print(i)
elif c=='down':
	for i in range(20,int(input('Enter number below 20')),-1):
		print(i)
else:
	print('Icant understand')
