#Challenge13
'''Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.'''
num=int(input('Enter number below 20:\n'))
print('Thank you' if num<20 else 'Too high')#inline if statement
