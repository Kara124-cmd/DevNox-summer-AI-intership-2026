

'''What is NumPy?
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.
'''

import numpy
arr = numpy.array([1,3,5,6,7])
print(arr)


# NumPy as np
# NumPy is usually imported under the np alias.

import numpy as np
arr = np.array([1,2,3,4,6])
print(arr)


# checking numpy version
import numpy as np
print(np. __version__)


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))



# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

import numpy as np
arr = np.array((1,2,4,6,7))
print(arr)




'''Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).
nested array: are arrays that have arrays as their elements.
'''

# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

import numpy as np
arr = np.array(42)
print(arr)


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.

import numpy as np
arr = np.array([1,3,5,6,7])
print(arr)

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.

import numpy as np
arr = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
print(arr)
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat



# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# check the number of dimensions using ndim
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)




# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.'''

import numpy as np
arr = np.array([1, 2, 3, 4, 5], ndmin = 5)
print(arr)
print('the number of dimension in arrys is : ', arr.ndim)




# access array element using indexes 
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[2])

# getting two element of the array and add them
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[0] + arr[2])


# accesing element in two-dimensional array
# the first element represent row and second represent columns

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])


# accesssing three dimensional array
import numpy as np
arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
print(arr)
print(arr[0, 0, 3])

# negative indexing in arrys
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, -1])




# array slicing 
import numpy as np
arr = np.array([1, 2, 4, 5, 6])
print(arr[1:4])
print(arr[:5])
print(arr[1:])
print(arr[-3:-1])

# steps in array
import numpy as np
arr = np.array([1, 2, 4, 5, 6, 9])
print(arr[1:6:2])
print(arr[::2])

# slicing two-dimensional array
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:4, 1])
print(arr[0:2, 1:4])




# data types in arrays
# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


import numpy as np
arr = np.array([1, 2, 3, 4, 5 ,6])
print(arr.dtype)


import numpy as np
arr = np.array(['apple', 'mango', 'banana', 'orange'])
print(arr.dtype)


# create array with a defined data type 
import numpy as np
arr = np.array([1, 3, 4, 5, 6], dtype = 'S')
print(arr)
print(arr.dtype)






# Numpy array vs View

# make copy change original and display both
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 8
print(arr)      # original 
print(x)        # copy array


#view
#  make view, change orignal and display both
import numpy as np 
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[2] = 9
print(arr)
print(x)




# print the shape of 2d arrya
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr.shape)


# create array of 5d array and return the shape
import numpy as np
arr = np.array([1, 2, 3, 4 ,5], ndmin = 5)
print(arr.shape)



# rashaping an numpy Array
# convert the 1D- array into 2D-array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_array = arr.reshape(3, 4)
print(new_array)


# reshape from 1D to 3D array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12])
new_array = arr.reshape(2,2,3)
print(new_array)

# return copy or view
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 8])
print(arr)
print(arr.reshape(3, 3).base)



# flattering an array
# convert the multi-dimension to 1D array 

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print(arr.reshape(-1))    # this conver the multi dimensinoal array into the 1D array


# what will it prints
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)



# iterating an array

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
for x in arr:
    print(x)


# iterating 2d array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:
    print(x)



# iterating through for each scalar element of 2d array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:
    for y in x:
        print(y)


# iteartin 3d array
import numpy as np
arr = np.array([[[1,2,3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)


# iterate each element in three dimension array
import numpy as np
arr = np.array([[[1,2,3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)


# this upper same iteration can be done through the nditor() function
# iterating array using nditor()
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# iterating array of nditor() using different step size
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)


# Enumerated Iteration Using ndenumerate()

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# enumrate on 2d array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)



# joining numpy array using concatenate() function

import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

result = np.concatenate((arr1, arr2))
print(result)



# joining 2D array along with row (axis = 1)
import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.concatenate((arr1, arr2), axis = 1)
print(arr)




# joining arrays using stack() functions
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.stack((arr1, arr2), axis = 1)
print(arr)



# stacking along rows using hstack
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.hstack((arr1, arr2))
print(arr)


# stacking along columsn
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.vstack((arr1, arr2))
print(arr)


# stacking along height (depth)
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.dstack((arr1, arr2))
print(arr)




# numpy splitting array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

newarr = np.array_split(arr, 3)
print(newarr)



# access the splitted arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])



#splitting 2D-array
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 2)
print(newarr)



# Split the 2-D array into three 2-D arrays along columns.

import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 2, axis = 1)
print(newarr)

# alternate to using along with columsn use hsplit() function

import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.hsplit(arr, 2)
print(newarr)


# vsplit ()
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.vsplit(arr, 2)
print(newarr)



# searching in arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


# find the index where the value are odd
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr % 2 == 1)
print(x)



# Find the indexes where the value 7 should be inserted:
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 9)

print(x)



# find the index where value 7 should be inserted starting from the right
import numpy as np
arr = np.array([6, 7, 1, 4, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)



# find the indexes where the value of the 2, 4, 7  should be inserted
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.searchsorted(arr, [2, 4, 7])
print(x)





'''Sorting Arrays
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified array.'''

# sort the array
import numpy as np
arr = np.array([1, 6, 0, 3, 9])
print(np.sort(arr))

### Note: This method returns a copy of the array, leaving the original array unchanged.####

# sort the array alphabetically
import numpy as np
arr = np.array(['Mango', 'Apple', 'Banana'])
x = np.sort(arr)
print(x)
print(arr)


# sort a boolean array
import numpy as np
arr = np.array([True, False, True])
x = np.sort(arr)
print(x)


# sort 2D-array
import numpy
arr = numpy.array([[1, 5, 3, 4], [8, 7, 6, 9]])
x = numpy.sort(arr)
print(x)

