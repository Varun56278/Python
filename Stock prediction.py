

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = pd.read_csv("NSE.csv")
print(a)

print(a.shape)
print(a['OPEN'].describe())


c = a.corr()
print(c)

print(a.head())

x = a['OPEN']
y = a['CLOSE']
print(x)
print(y)

x = np.array(x).reshape(-1,1)
print(x)

o = LinearRegression()
lm = o.fit(x, y)

print(lm)
print(lm.intercept_)
print(lm.coef_)

b = lm.predict(x)
print(b)

OPEN = []
for x in range(3):
    a = float(input('enter OPEN :'))
    OPEN.append(a)

OPEN = np.array(OPEN).reshape(-1,1)

print(lm.predict(OPEN))
