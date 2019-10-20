#Challenge29
'''Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two
decimal places.'''
import math
num=math.sqrt(int(input('Enter number greater than 500')))
print(f'{num:.2f}')