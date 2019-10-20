#Challenge33
'''Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).'''
num1=int(input('Enter a number:\n'))
num2=int(input('Enter a number:\n'))
print('{0} divided by {1} is {2} with {3}'.format(num1,num2,num1//num2,num1%num2))