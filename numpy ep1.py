import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(np.__version__)
print(type(arr))


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#index:
print(arr[0],arr[1])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,1])#you can also type arr[0][1]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Return every other element from index 1 to index 5:
print(arr[1:5:2])



#dtype
arr=np.array(['1','2','3',4],dtype='i4')
print(arr,arr.dtype)
arr=np.array([1,2,33],dtype='S')
print(arr,arr.dtype)


#astype() : the function creates a copy of the array, and allows you to specify the data type as a parameter.
new_arr=arr.astype(int)
print(new_arr)