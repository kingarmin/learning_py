import numpy as np

#search with where() :You can search an array for a certain value, and return the indexes that get a match.
arr=np.array([1,2,3,4,5,4,4])
print(arr)
x=np.where(arr==4)
print (x)

x = np.where(arr%2 == 0)
print(x)
#where(condition)

x=np.searchsorted(arr,4)
print(x) # the index of first "4

#np.sort()
arr=np.array([7,5,10,3])
print(arr,np.sort(arr))