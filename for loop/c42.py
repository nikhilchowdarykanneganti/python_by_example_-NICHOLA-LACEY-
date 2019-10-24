#Challenge42
'''Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.'''
total=0
for i in range(5):
	t=int(input('Enter a number:\n'))
	if input('What to add this to total(y/n):')=='y':
		total+=t
print('total={0}'.format(total))
