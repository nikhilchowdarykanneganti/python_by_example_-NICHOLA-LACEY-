#Challenge18
'''Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.'''
num=int(input('Enter a num:\n'))
print('Too low' if num<10 else('Correct' if num>=10 and num<20 else 'Too high'))