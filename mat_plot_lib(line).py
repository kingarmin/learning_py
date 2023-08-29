import matplotlib.pyplot
import numpy as np
x=np.array([50,100])#[start x , end x]
y=np.array([0,50])#[start y , end y]
print(x,y)
#by default, plot function draw a line frome point to point
matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()