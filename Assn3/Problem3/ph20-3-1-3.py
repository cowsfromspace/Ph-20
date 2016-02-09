import numpy as np
import matplotlib.pyplot as plt
import sys

#########
# SETUP #
#########
if len(sys.argv) == 5:
	# Allowing command-line arguments
	(n, h, v0, x0) = (float(x) for x in sys.argv[1:])
else:
	if len(sys.argv) == 2 and sys.argv[1].lower() == "help":
		print "Command line arguments are allowed:\n \
		Must be in form n h x0 v0\n \
		Default values: \n \
		n = 1000000\n \
		h = 0.0001\n \
		x0 = 0\n \
		v0 = 1"
	# Creating a default set of conditions
	n = 100000    
	h = 0.0001     
	x0 = 0
	v0 = 1

################
# CALCULATIONS #
################
pos = np.zeros(n)
vel = np.zeros(n)

# Augment is the array multiplied for the implicit form
# Explicit form lacks the factor of 1/(1 + h ** 2)
augment = 1/(1 + h ** 2) * np.array([[1, h], [-h, 1]])
motion  = np.array([x0, v0])

for i in np.arange(n):
	pos[i] = motion[0]
	vel[i] = motion[1]
	motion = augment.dot(motion)
t = h * np.arange(n)
# Here is the exact form
exactX = x0 * np.cos(t) + v0 * np.sin(t)
exactV = v0 * np.cos(t) - x0 * np.sin(t)

 
#############
# PROBLEM 3 #
#############

	
def problem3():
	'''Writes the error max to file Errors.txt; used alongside graphErrors.py'''
	myFile = open("Errors.txt", 'a')
	errX = exactX - pos
	errV = exactV - vel
	myFile.write("%f %f %f\n" % (h, max(errX), max(errV)))
	myFile.close()


if __name__ == "__main__":
	problem3()
