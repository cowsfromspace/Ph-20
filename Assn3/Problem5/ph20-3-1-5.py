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
posX = np.zeros(n)
velX = np.zeros(n)
posI = np.zeros(n)
velI = np.zeros(n)

# Augment is the array multiplied for the implicit form
# Explicit form lacks the factor of 1/(1 + h ** 2)
augment = 1/(1 + h ** 2) * np.array([[1, h], [-h, 1]])
motionX = np.array([x0, v0])
motionI  = np.array([x0, v0])
for i in np.arange(n):
	posX[i] = motionX[0]
	velX[i] = motionX[1]
	posI[i] = motionI[0]
	velI[i] = motionX[1]
	motionX = augment.dot(motionX)
	motionI = motionX * (1 + h ** 2)
t = h * np.arange(n)
# Here is the exact form
exactX = x0 * np.cos(t) + v0 * np.sin(t)
exactV = v0 * np.cos(t) - x0 * np.sin(t)

 
############
# PROBLEMS #
############


def problem2():
	'''Graphs x - x_approx versus t and v - v_approx versus t'''
	# First graph: x - x_approx
	plt.title("Position Error: n = %d, h = 0%s, x0 = %.1f, v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Error (Exact - Calculated)")
	plt.xlabel("Time")
	plt.plot(t, exactX - posX)
	plt.plot(t, exactX - posI)
	plt.show()

	# Second graph: v - v_approx
	plt.title("Velocity Error: n = %d, h = 0%s, x0 = %.1f, v0 = %.1f" % (n, str(h).strip('0'), x0, v0))
	plt.ylabel("Error (Exact - Calculated)")
	plt.xlabel("Time")
	plt.plot(t, exactV - velX)
	plt.plot(t, exactV - velI)
	plt.show()

def problem4():
	'''Calculates E for both exact and approximate'''
	eApprxE = np.sqrt(posX   ** 2 + velX   ** 2)
	eApprxI = np.sqrt(posI   ** 2 + velI   ** 2)
	eExact  = np.sqrt(exactX ** 2 + exactV ** 2)
	plt.ylabel("Energy")
	plt.xlabel("Time")
	plt.title("Energy Dissipation")
	plt.plot(t, eApprxE)
	plt.plot(t, eApprxI)
	plt.plot(t, eExact)
	plt.show()


if __name__ == "__main__":
	problem2()
	problem4()
