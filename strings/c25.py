#Challenge25
'''Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.'''
n=input('Enter name:\n')
print(n if len(n)>5 else n+input('Enter sur:\n'))