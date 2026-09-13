



'''Arrays in Numpy
A NumPy array (ndarray) is a collection of elements of the same data type stored in a multidimensional structure. Arrays provide an efficient way to store and perform operations on numerical data.

Number of dimensions in an array is called its rank.
Size of the array along each dimension is called its shape.
Elements are accessed using square brackets [] and arrays are commonly created from Python lists.'''



# List VS Numpy difference
# both have the operation like inseration, deletion, appending, concatenation etc
# but the main difference is the more in numpy like

# example:
#    list :--- >
a = [1, 2, 3]
b = [4, 5, 6]
a*b # cannot multiply

# but in Numpy we can multiply and many more
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4,5, 6])
print(a * b)





# first make 1D Array
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)


# create the 2D - array elements of float

import numpy as np
b = np.array([[1.0, 2.0, 2.2], [2.1, 4.5, 7.0]])
print(b)


# create a 1D-array of alphabet
import numpy as np
a = np.array(['apple', 'mango', 'banana', 'orange'])
print(a)

# 
import numpy as np
arr1 = ([1, 3, 5, 7, 9])
b = 2
print(arr1 * b)

import numpy as np
arr = np.array([
    [-1, 2, 0, 4],
    [4, -0.5, 6, 0],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2.0]
])
arr2 = arr[:2, ::2]
print("First 2 rows and alternate columns:\n", arr2)

# accessing each row and column specified [[row1, row2, row3, row4], [col1, col2, col3, col4]]
arr3 = arr[[1, 1, 0, 3], [3, 2, 1, 0]]
print("Selected elements:", arr3)


# take the transpose of matrix

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.T)


# Initialize a Python NumPy Array Using Special Functions
import numpy as np

a0 = np.zeros((2, 3))
a1 = np.ones((3, 3))
af = np.full((2, 2), 7)
ar = np.arange(0, 10, 2)  # start, stop, step
la = np.linspace(0, 8, 5)  # start, stop, num(how many number you want)

print("Zero Array:","\n",a0)
print("Ones Array:","\n",a1)
print("Constant Array:","\n",af)
print("Range Array:","\n",ar)
print("Linspace Array:","\n",la)



# Get dimension of array
import numpy as np
b = np.array([[1.0, 2.0, 2.2], [2.1, 4.5, 7.0]])
print(b)
print(b.ndim)

# get the shape of array
import numpy as np
b = np.array([[1.0, 2.0, 2.2], [2.1, 4.5, 7.0]])
print(b)
print(b.shape)

# get the type of array dtype
import numpy as np
b = np.array([[1.0, 2.0, 2.2], [2.1, 4.5, 7.0]])
print(b)
print(b.dtype)


# specify the type of array
import numpy as np
b = np.array([[1.0, 2.0, 2.2], [2.1, 4.5, 7.0]], dtype = 'int')
print(b)
print(b.dtype)



# accesssing the specific item in the array
import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
# [row , column]
print(arr[1,2])

# get the specific row
import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
print(arr[0, :])   #[firstrow, all columns]

# get the specific column
import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
print(arr[:, 2])   # [both rows, and the column at index 2]

# getting the specific items in the array

import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
print(arr[0, 1:4:2])     #[firstrow, firstindex:lastindex:stepsize]

# changing the element in array
import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
arr[1,3] = 99
print(arr)



# 3D-array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

print(arr[0,1,2])   # get specif elemtn

print(arr[:,1, 1]) # [bothTable, :1row, :column 1]

print(arr[1, 0, 2])  # [2ndTable, firstroww, 3columns]



# intitailize all zero matrix
import numpy as np
zeromatrix = np.zeros((2, 3,3))
print(zeromatrix)


# all ones matrix
import numpy as np
one = np.ones((4, 3))
print(one)

# print the random decimal number in matrix
import numpy as np
arr = np.random.random((3, 3))
print(arr)

# print the random integers number in matrix
import numpy as np
arr = np.random.random_integers(2, 7, size = (3, 3))
print(arr)

#print an identity matrix 
import numpy as np
identitye = np.identity(3)
print(identitye)

# repeart an array
import numpy as np
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis = 0)
print(r1)


# copying the content of array1 into array2 without chaning array1

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.copy()
arr2[0] = 9
print(arr1)
print(arr2)

# numpy has some mathematics capabitlites 
import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
print(arr + 2)
print(arr - 2)
print(arr * 2)
print(arr / 2)
print(arr ** 2)

cs = np.cos(arr)
print(cs)



# Reorganizing arrays
import numpy as np
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape(4, 2)
print(after)





# numpy random.normal vs random.rand

import numpy as np
arr = np.random.rand(4,4)
print(arr)

arrN = np.random.normal(0.0, 1.0, (3, 3, 2))       # normal([loc, scale, size(row, col, dim)])
print(arrN)








# ============================================== practice question s==============================================================

import numpy as np
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print(arr.shape)
print(arr.reshape(2, 8))
print(arr.ndim)

print(arr[2, 1])

print(arr[2])
print(arr[:, 1])

print(arr[0:2, 0:3])

print(arr[:3, ::2])



# fancy indexing
print(arr[[1, 3, 2], [1, 0, 3]])



import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))


# write a code that select only number that greater than 20 using boolean filtering
import numpy as np
arr = np.array([10, 15 , 20, 25, 30, 40])
new = arr >= 20
print(new)



import numpy as np
a = np.arange(2, 12, 2)     # [start, stop, step]
print(a)


import numpy as np
a = np.linspace(2, 10, 5)   #[start, stop , number]
print(a)


import numpy as np
rd = np.random.normal(1, 2, (3, 3))
print(rd)


import numpy as np
ide = np.array([10, 4, 8, 10, 12, 10])
idx = np.where(ide == 10)
print(idx)



'''Without changing the original array, produce:

[[ 2  4]
 [ 7  9]
 [12 14]]'''

import numpy as np
arr = np.array([
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

newarr = np.copy(arr)
print(newarr)
print(newarr[:3, 1:4:2])





# reverse the columns
import numpy as np

arr = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])
print(arr[:,::-1])
# reverse rows
print(arr[::-1])

print(arr[::2, ::2])

print(arr[1:3, 1:4])   # centre of array



# select all numbers between the 30 and 80 including
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
res = arr[(arr >= 30) & (arr <= 80)]
print(res)


# replace every number grater than 20 with 0
import numpy as np
arr = np.array([2, 25, 6, 20, 15, 30, 35])
res = np.where(arr > 20, 0, arr)
print(res)
mins = np.where(arr > 20, -1, arr)   # replace the value if there b any number greater than 20 with -1
print(mins) 






import numpy as np
a = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
])

# select the last 2 rows and first two columns
print(a[2:, :2])

# Select:
# rows 0 and 2
# columns 1 and 3
print(a[:3:2, 1:4:2])


print(a[[0, 2, 3]][:, [1, 3]])

print(a + 10)    # add 10 to every element 
print(a * 2)      # multipy every element by 2




import numpy as np
a = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
])

print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.mean(a))

# find all value greater than 20
res = a[np.where(a > 20)]
print(res)


# find the index poistion where the value is greater than 40
print(a > 40)

# replace every value less than 30 with 0
print(np.where(a < 30, 0, a))




import numpy as np
a =  np.array([
    [12, 25,  8, 40, 15],
    [30,  7, 50, 18, 22],
    [ 5, 35, 10, 45, 20],
    [28,  3, 60, 14, 32]
])

# get this
# [[25 40]
#  [35 45]
#  [28 60]]
 
result = a[[0, 0, 2, 2, 3, 3], [1, 3, 1, 3, 0, 2]].reshape(3, 2)

print(result)
























# pratice problems 
'''1. Create a NumPy Array
Create a NumPy array containing:
10, 20, 30, 40, 50

Print:
the array
its type
its number of dimensions
'''



#1
import numpy as np
mylist = [10, 20, 30, 40, 50]
arr = np.array(mylist)
print(arr)
print(type(arr))
print(arr.ndim)




# create a list convert it to numpy array and multiply each item by 3
#2
import numpy as np
mylist = [2, 4, 6, 8, 10]
arr = np.array(mylist)
print(arr * 3)



# create a tuple convert into array and type its dtype
#3
import numpy as np
mylist = [2, 3, 5, 7, 9]
arr = np.array(mylist)
print(arr.dtype)



# check dimnsion of each array
#4

import numpy as np
arr1 = np.array(42)
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# check dimesion 
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)



# create a array with dimesion 5 and print array its dimension and shape
#5
import numpy as np
arr = np.array([1, 2, 3, 4, 5], ndmin = 5)
print(arr)
print(arr.ndim)
print(arr.shape)



# create a array print 1st, third, last and second last element
#6 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[-2])

# 7  :   add 2 + 5 and print
print(arr[1] + arr[4])



# create 2D-array and indexing 
#8
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(arr[1,3])
print(arr[1,1])
print(arr[-1, -2])
print(arr[2, -3])


# creat the 2D-array and indexing
#9
import numpy as np
arr = np.array([
    [[1, 2, 3],[3, 4, 5]],
    [[7, 8, 9],[10, 11, 12]]
])

print(arr[1, 1, 2])
print(arr[0, 0, 1])
print(arr[0, -1, -2])
print(arr[1, 1, -3])






# 1D-array slicing specific elemnts
#10
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:5])
print(arr[:5])
print(arr[5:])
print(arr[::-1])


# 2D array slicing 
#11
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [14, 16, 18, 20]
])

print(arr[0,1:])
print(arr[1,1:3])
print(arr[2,::2])
print(arr[3,::-2])



# reverse the columns
#12
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [14, 16, 18, 20]
])

print(arr[::, ::-1])


# reverse the row
#13
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [14, 16, 18, 20]
])
print(arr[::-1])




#extract the centre of matrix
#14
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [14, 16, 18, 20]
])

print(arr[1:3, 1:3])




# find the dimension, shape and data type of 2D-array
#15
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [14, 16, 18, 20]
])

print(arr.ndim)
print(arr.shape)
print(arr.dtype)


# reshape of 1D array into 2D-array
#16
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = arr.reshape(3,3)
print(newarr)
print(newarr.ndim)



# now conver the same 1D into 3D array
#17
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.reshape(2,2,3))


# flatten the array
#18
import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.reshape(-1))



# create array using arange and reshape it different forms
#19
import numpy as np
arr = np.arange(1, 25)
print(arr)
print(arr.reshape(4, 6))
print(arr.reshape(2, 3, 4))


# create array containing int, float, strings and boolean and print dtype
#20
import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1.1, 2.0, 3.4, -2.3])
a3 = np.array(['a', 'b', 'c', 'd'])
a4 = np.array([True, False, True])

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
print(a4.dtype)
# change the float datatype to integer
fl_to_int = np.array(a2, dtype = int)
print(fl_to_int)





# change the any element of the copied array and print the original and copid both
# 21
import numpy as np
arr = np.array([1, 3, 5, 7, 8, 9])
newArr = np.copy(arr)
newArr[2] = 4
print(newArr)
print(arr)



# change the element of the view() and print the view and original array
#22
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
newArr = arr.view()
newArr[0] = 9
print(newArr)
print(arr)


#Create Special Arrays using numpy functions, 2X3 of zeros, 3X3 of ones and 2X3 full of 7
# 25. 
import numpy as np
arr1 = np.zeros((2,3))
arr2 = np.ones((3,3))
arr3 = np.full((2,3), 7)
print(arr1)
print(arr2)
print(arr3)


# create and arrange in this sequence 2, 4, 6, 8, 10, 12, 14
#26
import numpy as np
arr = np.arange(2,15,2)
print(arr)


# Generate exactly 6 equally spaced numbers between: 0 to 30
# 27
import numpy as np
arr = np.linspace(0,30,6)
print(arr)


# create the identity matric of 4X4
import numpy as np
arr = np.identity(4)
print(arr)




# 28. Random Arrays Create:
'''3 x 3 matrix of random decimal numbers
4 x 4 matrix of random numbers using np.random.rand()
3 x 3 matrix using np.random.normal()'''
import numpy as np
import random 
arr1 = np.random.random((3,3))
arr2 = np.random.rand(4, 4)
print(arr1)
print(arr2)


# array mathematics
#29
import numpy as np
arr = np.array([2, 4, 6, 8, 10])
print(arr + 5)
print(arr - 2)
print(arr * 2)
print(arr / 2)
print(arr ** 2)



# methamatic operations on two array
#30
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)
print(a - b)
print(a * b)
print(a / b)



# create a matrix and transpose it 
#31
import numpy as np
arr1 = np.array([[1, 2, 3], [5, 6, 7]])
print(np.transpose(arr1))



# print every element using for loop
#32
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
for i in arr:
    print(i)


# print the 2D-array using iteration
#33
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for row in arr:
    for element in row:
        print(element, end = " ")

    print()


# print the 3D-array using loop
#34
import numpy as np
arr = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])

for block in arr:
    for row in block:
        for element in row:
            print(element, end=' ')



# now take the same arry and use the nditor()
#35
import numpy as np
arr = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])
for element in np.nditer(arr):
    print(element, end = ' ')



# nditor plus slicing
#36
import numpy as np
arr = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])

for element in np.nditer(arr[:, ::2]):
    print(element)


# enumerate 
#37
import numpy as np
arr = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])

for idx, element in np.ndenumerate(arr):
    print(idx, element)


# joining array
#38
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(np.concatenate((arr1, arr2)))


# stack opeartion (stack, hstack, vstack, dstack)
#39
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

#.stack
result0 = np.stack((arr1, arr2), axis=0)
result1 = np.stack((arr1, arr2), axis=1)
print(result0)
print(result1)

#.hstack 
stk = np.hstack((arr1, arr2))
print(stk)
# .vstack
stkv = np.vstack((arr1, arr2))
print(stkv)

# dstack
print(np.dstack((arr1, arr2)))





# split 1D array into 4 arrays
#40
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
spArr = np.array_split(arr, 4)
print(spArr)



# split 2d Array into 2 arrays along rows
#41
import numpy as np
arr = np.array([
    [1,2],
 [3,4],
 [5,6],
 [7,8],
 [9,10],
 [11,12]
])

newArr = np.array_split(arr, 2, axis = 1)
print(newArr)



# hsplit() vs vsplit()
#42
import numpy as np
arr = np.array([
    [1,2],
 [3,4],
 [5,6],
 [7,8],
 [9,10],
 [11,12]
])

HArr = np.hsplit(arr, 2)
print(HArr)
VArr = np.vsplit(arr,2)
print(VArr)


#searching : find the index where value is 20
#43
import numpy as np
arr = np.array([10,20,30,20,40,20,50])
print(np.where(arr == 20))



# find the indexes where odd number exist
#44
import numpy as np
arr = np.array([10,21,30,20,45,20,50])
idx = np.where(arr % 2 == 1)
print(idx)



# find value greater than 30 using boolean filtering and np.where
#45
import numpy as np
arr = np.array([4, 40, 15, 20, 15, 30, 35])
print([arr > 20])
print(np.where(arr > 20))


# find the insertion position where 35 should be inserted using searchsort
#46
import numpy as np
arr = np.array([10,20,30,40,50])
print(np.searchsorted(arr, 35))



# find the multiple search values 
#47
import numpy as np
arr = np.array([10,20,30,40,50])
print(np.searchsorted(arr, (21, 35, 55)))



# search value betweeen 20 to 40 using boolean filtering
#48
import numpy as np
arr = np.array([10, 45, 20, 30, 5, 21, 50, 18])
print(arr[2:6])
# replace value that are greater than 0
print(np.where(arr > 20, 0, arr))
# now the value that are greater than 20 replace with -1
print(np.where(arr > 20, -1, arr))



# Find every value greater than 25 in Matrix filtering
#49
import numpy as np
arr = np.array([
    [10, 25, 30],
    [5, 40, 15],
    [50, 20, 35]
])

print(arr[arr > 25])
# replace every value less than 20 with 0
print(np.where(arr < 20, 0, arr))






#sort 1d array of numbers, strings, boolean and 2d array
#50
import numpy as np
arr1 = np.array([20, 12, 6, 5, 10, 15])
arr2 = np.array(['mango', 'banana', 'apple', 'cherry'])
arr3 = np.array([True, False, True, False])
print(np.sort(arr1))
print(np.sort(arr2))
print(np.sort(arr3))



# find the minimum, maximum, sum, and average(mean)
#51

import numpy as np
arr = np.array([
    [5,10,15,20],
    [25,30,35,40],
    [45,50,55,60]
])

print(np.min(arr))
print(np.max(arr))
print(np.sum(arr))
print(np.average(arr))
# find the index where values are greater than 40 and all values greater than 30
print(np.where(arr > 40))
print(arr[arr > 30])




# select the 60 , 40 and 130
#52
import numpy as np
arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120],
    [130,140,150,160]
])

newArr = arr[[1, 0, 3], [1, 3, 0]]
print(newArr)
# # also you can specify the index before print
row = [1, 0, 3]
cols = [1, 3, 0]
print(arr[row, cols])


# select the row(0,2), col(1, 3)
print(arr[[0, 2], [1, 3]])




# student marks
# 53
import numpy as np
marks = np.array([
    [78, 85, 92, 66],
    [55, 73, 81, 90],
    [88, 91, 76, 84]
])

print(marks.shape)
print(marks.ndim)
print(np.min(marks))
print(np.max(marks))
print(np.average(marks))
print(marks[marks > 80])
print(np.where(marks > 80))

#replace every marks below 60 with 0
newArr = np.where(marks < 60, 0, marks)
print(newArr)
print(marks)




# numpy Data Analysis
import numpy as np
data = np.array([
    [10, 25, 30, 45, 50],
    [15, 35, 20, 55, 60],
    [5,  40, 70, 30, 80],
    [25, 10, 90, 35, 65]
])

# basic information
'''print(data.ndim)
print(data.shape)
print(data.dtype)'''

# selection
'''print(data[:2])
print(data[:,3:])
print(data[:, ::-1])'''

# filtering
'''print(data[data > 50])
print(np.where(data > 50))
print(data[(data > 20) & (data < 60)])
'''

# replacement
'''repArr = np.where(data < 20, 0, data)
print(repArr)'''


# mathematics
'''print(data + 10)
print(data * 3)
'''
# statistics
'''print(np.min(data))
print(np.max(data))
print(np.average(data))
print(np.sum(data))

'''

# reshape
reArr = data.reshape((2,10))
print(reArr)

print(reArr.flatten())    # flatten into 1 dimension

print(np.sort(reArr))







#complete numpy mini project student marks
import numpy as np
students = np.array([
    [78, 92, 65, 88, 55],
    [90, 85, 72, 95, 80],
    [45, 60, 55, 70, 50],
    [88, 91, 89, 94, 96],
    [62, 75, 68, 70, 77]
])

print(students)
print(students.ndim)
print(students.dtype)
print(students.shape)
print(np.min(students))
print(np.max(students))
print(np.average(students))
print(np.sum(students))
print(students[students > 80])
print(np.where(students > 80))
print(np.where(students < 50, 0, students))
newarr = np.copy(students)
print(newarr)

for marks in np.nditer(newarr):
    print(marks, end = ' ')

for idx, val in np.ndenumerate(newarr):
    print(idx, val)