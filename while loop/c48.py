#Challenge48
'''Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
coming to the party.'''
c=0
while input('What to invite a member(y/n):\n')=='y':
	print(input('Enter name:\n'),'is invited!\n')
	c+=1
print('Total',c,'members are invited.')