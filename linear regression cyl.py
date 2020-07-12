import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = pd.read_csv("mn.csv")
print(a)
print(a.shape)
print(a['mpg'].describe())

c = a.corr()
print(c)

print(a.head())

x = a['mpg']
y = a['cyl']
print(x)
print(y)

x = np.array(x).reshape(-1,1)
print(x)


o = LinearRegression()
lm = o.fit(x,y)

print(lm)
print(lm.intercept_)
print(lm.coef_)

b = lm.predict(x)
print(b)


mpg = []
for x in range(3):
    a = int(input('enter mpg :'))
    mpg.append(a)

mpg = np.array(mpg).reshape(-1,1)

print(lm.predict(mpg))






