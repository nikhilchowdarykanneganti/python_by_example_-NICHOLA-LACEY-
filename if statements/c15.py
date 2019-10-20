#Challenge15
'''Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.'''
col=input('Enter your fav color\n').lower()
print('I like red too' if col=='red' else 'I prefer red')