import random
import numpy as np
data = []

for x in range(5000):
    r = random.randint(0,1)
    data.append(r)


#print(data)

n = np.array(data)

print(n)
print(n.shape)


size = int(input('size  :'))

import math
s = math.sqrt(size)
mat_size = int(s)
print(mat_size)


mat = []
i = 0
for r in range(mat_size):
    row=[]
    for c in range(mat_size):
        row.append(data[i])
        i=i+1
    mat.append(row)



######
if (mat_size**2)<size:
    temp = []
    for r in range(0, size - (mat_size**2)):
        temp.append(data[i])
        i =i+1


    for r in range(0, ((mat_size+1)**2)- size):
        temp.append(0)


    print(temp)


    print("square matrix \n",mat)
    print("short data \n",temp)

    #last row 
    new_mat=[]
    j=0
    for i in range (0,mat_size+1):
            new_mat.append(temp[j])
            j=j+1

    print("last row \n ",new_mat)
    #end of last row
    
    for ind in range(0,len(mat)):
        mat[ind].append(temp[j])
        j=j+1

    print("after add last col \n",mat)

    #add last row 
    mat.append(new_mat)

print("perfect matrix \n ")
for row in mat:
    print(row)
    


