#Challenge17
'''Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.'''
age=int(input('Enter age:\n'))
print('You can vote' if age>=18 else('You can lear to drive' if age==17 else('You can buy lottery' if age==16 else 'You can go trick or treat')))