import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
color=np.array([0,10,50,20])
size=np.array([20,50,80,1000])
plt.scatter(x,y,c=color,alpha=0.5,s=size)#alpha--->ghost
plt.colorbar()#show color bar

plt.title("scotter")
plt.show()