import matplotlib.pyplot as plt
import numpy as np

y=np.array([0,40,90,100,200])
plt.plot(y)
plt.xlabel("X positain")
plt.ylabel("y position")
plt.title("matplotlib test")
#plt.grid(axis='y')
#plt.grid(axis='x')
plt.grid()
plt.show()