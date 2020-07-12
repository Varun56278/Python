import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

a = pd.read_csv("horse.csv")
print(a)
print(a.shape)
print(a.describe())

print(a.corr())

plt.scatter(a['Mileage'],a['Sell Price'])
plt.show()


plt.scatter(a['Age(yrs)'],a['Sell Price'])
plt.show()

X = a[['Mileage','Age(yrs)']]
print(X)
Y = a['Sell Price']
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3)

print(len(X))

print(len(X_test))

print(X_test)
print(X_train)
