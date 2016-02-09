import numpy as np
import matplotlib.pyplot as plt
import sys

#########
# SETUP #
#########
n, h, v0, x0 = 100000, 0.0001, 0, 1 # Creating a default set of conditions

def setup():
	global n, h, v0, x0
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
setup()

################
# CALCULATIONS #
################
posX = np.zeros(n)
velX = np.zeros(n)
posI = np.zeros(n)
velI = np.zeros(n)

#HERE IS THE ORIGINAL IMPLICIT DEFINITION
# Augment is the array multiplied for the implicit form
# Explicit form lacks the factor of 1/(1 + h ** 2)

augmentX = np.array([[1, h], [-h, 1]]) * 1#/(1 + h ** 2)
augmentI = np.array([[1, h], [-h, 1]]) * 1 /(1 + h ** 2)
motionX  = np.array([x0, v0])
motionI  = np.array([x0, v0])

for i in np.arange(n):
	posX[i] = motionX[0]
	velX[i] = motionX[1]
	posI[i] = motionI[0]
	velI[i] = motionI[1]
	motionX = augmentX.dot(motionX)
	motionI = augmentI.dot(motionI)


# Here is the symplectic form
posS = np.zeros(n)
velS = np.zeros(n)
motionS = np.array([x0,v0])
trans1  = np.array([[1, h],[0,  1]])
trans2  = np.array([[1, 0],[-h, 1]])

for i in np.arange(n):
	posS[i] = motionS[0]
	motionS = trans1.dot(motionS)
	velS[i] = motionS[1]
	motionS = trans2.dot(motionS)


# Here is the exact form
t = h * np.arange(n)
exactX = x0 * np.cos(t) + v0 * np.sin(t)
exactV = v0 * np.cos(t) - x0 * np.sin(t)

 
############
# PROBLEMS #
############
def problem1():
	'''Graphs phase space of data. Also used in problem 2'''
	plt.plot(velX,    posX,    'b')
	plt.plot(velI,    posI,    'r')
	plt.plot(exactV,  exactX,  'g')
	plt.title("Vel & Pos: n = %d,  h = 0%s,  x0 = %.1f,  v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Position")
	plt.xlabel("Vel")
	plt.show()

def problem3():
	'''Calculates E for all 4 methods'''
	eApproxS = posS   ** 2  + velS   ** 2
	eApproxX = posX   ** 2  + velX   ** 2
	eApproxI = posI   ** 2  + velI   ** 2
	eExact   = exactX ** 2  + exactV ** 2
	plt.ylabel("Energy")
	plt.xlabel("Time")
	plt.title("Energy Dissipation")
	plt.plot(t, eApproxX, t, eApproxI)
	plt.plot(t, eExact)
	plt.show()

def problem4():
	k = (n - 100.0) / n
	plt.ylabel("Position")
	plt.xlabel("time")
	plt.title("Symplectic Position mistakes:  n = %d,  h = 0%s,  x0 = %.1f,  v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.plot(t[k * n::], posS[k * n::], t[k * n::], exactX[k * n::])
	plt.show()

	plt.ylabel("Velocity")
	plt.xlabel("time")
	plt.title("Symplectic Velocity mistakes: n = %d,  h = 0%s,  x0 = %.1f,  v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.plot(t[k * n::], posS[k * n::], t[k * n::], exactX[k * n::])
	plt.show()


if __name__ == "__main__":
	problem3()
