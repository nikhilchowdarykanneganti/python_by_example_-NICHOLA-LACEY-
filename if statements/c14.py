#Challenge14
'''Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.'''
num=int(input('Enter number b/w 10 and 20:\n'))
print('Thank you' if num<=20 and num>=10 else 'Incorrect answer')