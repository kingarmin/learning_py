import matplotlib.pyplot as mp
import numpy as np

y=np.array([3,5,10,50,60])
mp.plot(y,"x:b")#If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 //then change mark|line|color   "b"=blue
for index,i in enumerate(y):
    y[index]=i+20
mp.plot(y,"o--r")
mp.show()