import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

a = pd.read_csv("Card.csv")
print(a)

print(a.head())

x = a[['AGE']]
print(x)

y = a[['BILL_AMT1']]
print(y)

x = np.array(x).reshape(-1,1)
print(x)

tree = RandomForestRegressor(n_estimators = 100, random_state = 0) 

c = tree.fit(x,y)
print(c)


b = c.predict(x)
print(b)


AGE = []
for x in range(3):
    z = int(input('enter AGE :'))
    AGE.append(z)

AGE = np.array(AGE).reshape(-1,1)

print(c.predict(AGE))







