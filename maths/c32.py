#Challenge32
'''Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.'''
import math
print(round(float(input('Enter radius:\n'))*math.pi**2*float(input('Enter depth:\n')),3))