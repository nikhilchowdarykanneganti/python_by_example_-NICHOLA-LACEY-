#Challenge34
'''Display the following message:
1.sqare
2.triangle

enter a number:

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.'''

num=int(input('1.Square\n2.Triangle\nEnter a number:\n'))
if num==1:
	print('{0}'.format(int(input('Enter length:\n'))*4))
elif num==2:
	print('{0}'.format(int(input('Enter base:\n'))*int(input('Enter height:\n'))*0.5))
else:
	print('Choose a given option')