import numpy as np


#The Difference Between Copy and View
arr=np.array([1,2,3,4,5])
arr_view = arr.view()
print(arr,'\t',arr_view)
arr[0]=10
print(arr,'\t',arr_view)
#a view of an array is just a view of orginal array !!!

#copy
arr=np.array([1,2,3,4,5])
new_arr=arr.copy()
print(arr,'\t',new_arr)
arr[0]=10
print(arr,'\t',new_arr)