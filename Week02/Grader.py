from math import *

def polysum(n, s):
	'''
	n is an integer, number of sides of a polygon
	s is a float, the length of each side 

	return the sum of area and the square of the perimeter of the polygon
	'''
	area = (0.25 * n * s**2)/(tan(pi/n))
	perim = n*s

	return (round(area + perim**2,4))