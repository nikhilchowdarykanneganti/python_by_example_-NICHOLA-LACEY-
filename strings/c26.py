#Challenge26
'''Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.'''
w=input('Enter the word:\n')
if w[0] in 'aeiou':
	print((w+'way').lower())
else:
	print((w[1:len(w)-1]+w[0]+'ay').lower())
