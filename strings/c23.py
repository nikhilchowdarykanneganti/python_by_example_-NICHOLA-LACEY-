#Challenge23
'''Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text'''
rhyme=input('Enter a rhyme"\n')
print(len(rhyme))
s=int(input('Enter start:\n'))
e=int(input('Enter end:\n'))
print(rhyme[s:e])