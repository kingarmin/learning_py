import matplotlib.pyplot
import numpy as np
x=np.array([50,100])#[start x , end x]
y=np.array([0,50])#[start y , end y]
print(x,y)
#Now, plot function draw points!!
matplotlib.pyplot.plot(x,y,'o')

x=np.array([0,5,12,100])#[start x , end x]
y=np.array([100,5,12,6])#[start y , end y]
matplotlib.pyplot.plot(x,y)#draw a diagram
matplotlib.pyplot.show()