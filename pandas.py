import pandas as pd
import numpy as np 
dict1 = {
    "name":['harry','rohan','shubham','meenal'],
    "marks":[34,78,45,93],
    "city":['india','us','uk','aus']
    }
u = pd.DataFrame(dict1)
print(u)
u.index = ['a', 'b', 'c', 'd']
print(u)

print(u.head(2))
print(u.tail(2))

print(u.describe())

ser = pd.Series(np.random.rand(34))
print(ser)
o = type(ser)
print(o)

df = pd.DataFrame(np.random.rand(345,5))
print(df)

m = pd.DataFrame(np.random.rand(345,5))
print(m.head())

print(type(m))
print(m.describe())

print(df.dtypes)

l = df[0][0] = "Sachin"
a = df.dtypes
print(a)

print(df.head())
print(m.T)

#row
q = df.sort_index(axis=0, ascending=False)
print(q)

#column
q = df.sort_index(axis=1, ascending=False)
print(q)

