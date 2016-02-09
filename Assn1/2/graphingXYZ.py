import numpy as np
import matplotlib.pyplot as plt
import sys

'''
Will plot the data from one file as implemented in the system arguments.
'''

g = open(sys.argv[1], 'r')
v = []
for l in g:
	v.append(float(l))
g.close()

plt.plot(v)
plt.show()