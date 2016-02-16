import numpy as np
import matplotlib.pyplot as plt
import sys

#########
# SETUP #
#########
n, h, v0, x0 = 100000, 0.0001, 0, 1 # Creating a default set of conditions
problemNum = 0

def setup():
	global n, h, v0, x0, problemNum
	if len(sys.argv) == 6:
		# Allowing command-line arguments
		(n, h, v0, x0, problemNum) = (float(x) for x in sys.argv[1:])
		
	elif len(sys.argv) == 2 and sys.argv[1].lower() == "help":
		print "Command line arguments are allowed:\n \
		Must be in form n h x0 v0 probNum\n \
		Default values: \n \
		n = 1000000\n \
		h = 0.0001\n \
		x0 = 0\n \
		v0 = 1\n \
		problemNum = 0 (does all)"
		raise Exception;
setup()

################
# CALCULATIONS #
################
posX = np.zeros(n)
velX = np.zeros(n)
posI = np.zeros(n)
velI = np.zeros(n)

augmentX = np.array([[1, h], [-h, 1]])
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

# Here is the exact form
t = h * np.arange(n)
exactX = x0 * np.cos(t) + v0 * np.sin(t)
exactV = v0 * np.cos(t) - x0 * np.sin(t)

 
############
# PROBLEMS #
############
def problem1():
	'''Graphs x & x_approx versus t and v & v_approx versus t'''
	# First graph: x & x_approx
	plt.plot(t, posX, 'b')
	plt.plot(t, posI, 'g')
	plt.plot(t, exactX, 'r')
	plt.title("Position: n = %d,  h = 0%s,  x0 = %.1f,  v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Position")
	plt.xlabel("Time")
	plt.savefig('x-%d-%s-%d-%d' % (n, str(h).strip('0').strip("."), x0, v0), bbox_inches='tight')
	plt.clf()

	# Second graph: V & V_approx
	plt.title("Velocity: n = %d, h = 0%s, x0 = %.1f, v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Velocity")
	plt.xlabel("Time")
	plt.plot(t, velX, 'b')
	plt.plot(t, velI, 'g')
	plt.plot(t, exactV, 'r')
	plt.savefig('v-%d-%s-%d-%d' % (n, str(h).strip('0').strip("."), x0, v0), bbox_inches='tight')
	plt.clf()

def problem2():
	'''Graphs x - x_approx versus t and v - v_approx versus t'''
	# First graph: x - x_approx
	plt.title("Position Error: n = %d, h = 0%s, x0 = %.1f, v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Error (Exact - Calculated)")
	plt.xlabel("Time")
	plt.plot(t, exactX - posX, 'b')
	plt.plot(t, exactX - posI, 'g')
	plt.savefig('ErrX-%d-%s-%d-%d' % (n, str(h).strip('0').strip("."), x0, v0), bbox_inches='tight')
	plt.clf()

	# Second graph: v - v_approx
	plt.title("Velocity Error: n = %d, h = 0%s, x0 = %.1f, v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Error (Exact - Calculated)")
	plt.xlabel("Time")
	plt.plot(t, exactV - velX, 'b')
	plt.plot(t, exactV - velI, 'g')
	plt.savefig('ErrV-%d-%s-%d-%d' % (n, str(h).strip('0').strip("."), x0, v0), bbox_inches='tight')
	plt.clf()
	
#######################################################
# This new content is pretty useful for Makefile use; #
# should use a switch, but this is easier             #
#######################################################

if __name__ == "__main__":
	if problemNum == 1:
		problem1()
	if problemNum == 2:
		problem2()
