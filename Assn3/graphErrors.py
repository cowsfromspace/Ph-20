import numpy as np
import matplotlib.pyplot as plt

f = open("Errors.txt", 'r')
hArr, xArr, vArr = ([] for i in range(3))
for line in f:
	(h, x, v) = tuple(line.split())
	hArr.append(float(h))
	xArr.append(float(x))
	vArr.append(float(v))

plt.title("X stuff")
plt.xlabel("h")
plt.ylabel("x Error")
plt.plot(hArr, xArr)
plt.show()


plt.title("V stuff")
plt.xlabel("h")
plt.ylabel("v Error")
plt.plot(hArr, vArr)
plt.show()
