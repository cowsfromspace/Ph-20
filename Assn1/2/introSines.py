# Physics 20, Lab 1
# Jake Mattinson
# 5 January 2015

'''
Generates and then outputs sinusoids & their sum. 
Requires system input of all variables. 
X(t) = AX cos(2pifXt), (2)
Y (t) = AY sin(2pifY t + phi), (3)
Z(t) = X(t) + Y (t)
'''

import sys
from math import sin, cos, pi

def x(aX, fX, t):
	return aX * cos(2*pi*fX*t)

def y(aY, fY, phi, t):
	return aY * sin(2*pi*fY*t + phi)

def z(x, y):
	return x + y


if __name__ == "__main__":
	if len(sys.argv) != 8:
		raise Exception("Inputs wrong: fX, fY, aX, aY, phi, dt, N")

	# Setting all variables to initial status
	fX, fY, aX, aY, phi, dt, N = (float(x) for x in sys.argv[1:])
	N = int(N)
	xt, yt, zt = 0, 0, 0 # Just declaring the variables for now
	t = 0
	xList, yList, zList = [], [], []

	# Calculating all x, y, z
	for n in range(N):
		xt = x(aX, fX, t)
		yt = y(aY, fY, phi, t)
		zt = z(xt, yt)
		t += dt
		xList.append(xt)
		yList.append(yt)
		zList.append(zt)

	# Making the files, etc.
	xFile, yFile, zFile = open("x.txt", 'w'), open('y.txt', 'w'), open('z.txt', 'w')
	for n in range(N):
		xFile.write("%f\n" % xList[n])
		yFile.write("%f\n" % yList[n])
		zFile.write("%f\n" % zList[n])
	xFile.close()
	yFile.close()
	zFile.close()
