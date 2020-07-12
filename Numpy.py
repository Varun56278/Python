
import numpy as np
b = [11,222,44,55,663]
print(b)
print(type(b)) #list
x = np.array(b)
print(x)
print(type(x))

#array operation
print(b*2) #list operation
print(x*2) #array array
print(x.shape)





import numpy as np
a = [[1,2,4,],[1,32,44,],[1,2,4,]]
b = [[11,2,41,],[1,2,4,],[1,2,4,]]
x = np.array(a)
y = np.array(b)
print(x)
print(y)


print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))



#Numpy Defining Multi Dimensional Array
import numpy
arr = numpy.ndarray(shape=(3,3,3), dtype=int)

val=1
x = arr.shape[0] 
y = arr.shape[1]
z = arr.shape[2]
for i in range (x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k]=val
            val=val+1
print("Array element :")
print(arr)

#Numpy Reading element into matrix
import numpy

m = int(input("Enter row size :"))
n = int(input("Enter column size :"))
matrix = numpy.ndarray(shape=(m,n) , dtype=int)

print("Enter %d elements of %dx%d matrix :" %(m*n,m,n))
for i in range (m):
    for j in range(n):
        matrix[i][j]=int(input())
print("%dx%d matrix is : " %(m,n))
print(matrix)




#Numpy Creating Two Dimensional Array
import numpy

m = int(input("Enter row size :"))
n = int(input("Enter column size :"))
matrix = numpy.ndarray(shape=(m,n) , dtype=int)

print("Size :", matrix.size)
print("Shape :", matrix.shape)
print("Dimensions :", matrix.ndim)




#Numpy Creating One Dimensional Array

import numpy

n = int(input("enter the value"))
arr = numpy.ndarray(shape =(n), dtype = int)
print("enter %d element :" %n)

for i in range (n):
    arr[i] = int(input())
    
print("Array element :", arr)



#Numppy Submatrix from Matrix using Slicing

import numpy
a = [[10,20,30],[40,50,60],[70,80,90]]
matrix = numpy.array(a)
print(matrix)

#[row_lwr : row_upp , col_low : col_upp]

res = matrix[ : , : ]
print(res)
print()

res = matrix[ 0:3 , 0:3 ]
print(res)
print()

res = matrix[ 0:2 , 0:3 ]
print(res)
print()

res = matrix[ 0:3 , 0:2 ]
print(res)
print()


res = matrix[ 1:3 , 1:3 ]
print(res)
print()


    
#Numpy Array List
import numpy as np
a = [10,20,30,40,50,60,70,80,90]
arr = np.array(a)
print("Elements :")
for ele in arr:
    print(ele)

#Numpy Array List multi dimensional
import numpy as np
a = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(a)
print("Elements :")
#print(matrix)
for row in matrix:
    for ele in row:
          print(ele, end=' ')
    print()
    




#multi dimensional

import numpy
a = [[10,20,30],[40,50,60],[70,80,90]]
matrix = numpy.array(a)
print("Matrix :",matrix)
print("Size :",matrix.size)
print("Datatype :",matrix.dtype)
print("Dmension :",matrix.ndim)
print("Shape :",matrix.shape)


#one dimensional
import numpy
a = [1,2,3,4,5,6,7,8,9]
arr = numpy.array(a)
print("Array :",arr)
print("Size :",arr.size)
print("Datatype :",arr.dtype)
print("Dmension :",arr.ndim)
print("Shape :",arr.shape)
