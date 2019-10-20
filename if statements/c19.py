#Challenge19
'''Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.'''
num=int(input('ENter 1 2 or 3:\n'))
print('Thankyou' if num==1 else('Well done' if num==2 else('Correct' if num==3 else 'Error message')))