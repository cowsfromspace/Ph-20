# Physics 20, Lab 1
# Jake Mattinson
# 5 January 2015

'''
Generates and then outputs sinusoids and their sum. 
Requires system input of all variables.  
X(t) = AX cos(2pifXt), (2)
Y (t) = AY sin(2pifY t + phi), (3)
Z(t) = X(t) + Y (t)
'''

import sys
import numpy as np 
from math import sin, cos, pi

def x(aX, fX, t):
	return aX * cos(2*pi*fX*t)

def y(aY, fY, phi, t):
	return aY * sin(2*pi*fY*t + phi)

def z(x, y):
	return x + y


if __name__ == "__main__":
	if len(sys.argv) != 8:
		raise Exception("Inputs wrong: Should be of form \n fX  fY  aX  aY  phi  dt  N")

	# Setting all variables to initial status
	fX, fY, aX, aY, phi, dt, N = (float(x) for x in sys.argv[1:])
	N = int(N)
	(xArray, yArray, zArray) = (np.arange(0, dt * N, dt) for x in range(3))

	# Calculating all x, y, z
	xArray = aX * np.cos(2 * pi * fX * xArray)
	yArray = aY * np.sin(2 * pi * fY * yArray + phi)
	zArray = xArray	+ yArray
	
	# Making the files, etc.
	xFile = np.savetxt('x.txt', xArray) 
	yFile = np.savetxt('y.txt', yArray)
	zFile = np.savetxt('z.txt', zArray)
	tFile = np.savetxt('t.txt', np.arange(0, N * dt, dt))
	
