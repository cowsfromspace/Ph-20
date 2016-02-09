import numpy as np
import matplotlib.pyplot as plt
from math import e

def trap(func, a, b, N):
	'''Integrates a function func from a to b using 
	trapezoidenal rule in N divisions.'''
	h = float(b - a) / N
	vals = func(np.arange(a, b, h))
	return h * np.sum(vals[::2] + vals[1::2])

def simps(func, a, b, N):
	''' Integrates a function func from a to b using
	Simpson's rule in N divisions.'''
	h = float(b - a) / N
	area = 2 * h / 6 * (func(a) + func(b)) 
	vals = func(np.arange(a, b , h))
	area += 4 * 2 * h / 6 * np.sum(vals[1::2]) 	
	area += 2 * 2 * h / 6 * np.sum(vals[2::2])
	return area

def generateErrors(func, actual):
	'''Generates a bunch of error estimates for the integral from 0 to 1 of func
	This then graphs the log(error) v log(N).
	'''
	tArray = np.arange(40, 3000, 40)
	a = [abs((actual - trap(func, 0, 1, t))) / actual for t in tArray]
	print "a is calculated"
	b = [abs((actual - simps(func, 0, 1, t))) / actual for t in tArray]
	plt.plot(tArray, a, tArray, b)
	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel("N")
	plt.ylabel("Error")
	plt.title("Error of Simpson's Rule versus Trapezoid Rule")
	plt.show()

def arbitraryPrecision(func, a, b, N, error):
	'''Creates an integral that is within error of the previous approximation.'''
	N0 = N
	oldGuess = simps(func, a, b, N)
	N *= 2
	newGuess = simps(func, a, b, N)
	while( abs((oldGuess - newGuess) / oldGuess) > error):
		oldGuess = newGuess
		N *= 2
		newGuess = simps(func, a, b, N)
	return newGuess 
