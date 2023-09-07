import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
color=np.array(['red','blue','pink','black'])
plt.subplot(3, 1, 1)
plt.scatter(x,y,c=color)
plt.title("scotter")
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(3, 1, 3)
plt.plot(x,y,'o')
plt.title("plot(x,y,'o)")

plt.show()