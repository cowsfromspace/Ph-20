import numpy as np
import matplotlib.pyplot as plt
import sys

'''
Presumes there are files called x.txt, y.txt, z.txt.
Plots x v y and then plots z. 
'''

dataX = np.loadtxt('x.txt')
dataY = np.loadtxt('y.txt')
dataZ = np.loadtxt('z.txt')
dataT = np.loadtxt('t.txt')

plt.plot(dataX, dataY)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(dataT, dataZ)
plt.xlabel('t')
plt.ylabel('z')
plt.show()