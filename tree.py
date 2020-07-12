import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


a = pd.read_csv("wine.csv")
print(a)

print(a.head())

x = a[['alcohol']]
print(x)

y = a[['quality']]
print(y)

x = np.array(x).reshape(-1,1)
print(x)

tree = DecisionTreeClassifier()

c = tree.fit(x,y)
print(c)


b = c.predict(x)
print(b)


tree.plot_tree(c)
plt.show()


alcohol= []
for x in range(3):
    z = int(input('enter alcohol :'))
    alcohol.append(z)

alcohol = np.array(alcohol).reshape(-1,1)

print(c.predict(alcohol))







