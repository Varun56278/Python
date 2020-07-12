import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score




a = pd.read_csv("wine.csv")
print(a)

print(a.head())

x = a[['alcohol']]
print(x)

y = a[['quality']]
print(y)

x = np.array(x).reshape(-1,1)
print(x)

tree = LDA(n_components=1)
c = tree.fit(x,y)
print(c)


b = c.predict(x)
print(b)

f = classification_report(y ,b)
print(f)



m = confusion_matrix(y ,b)
print(m)

n = accuracy_score(y ,b)
print(n)


alcohol= []
for x in range(3):
    z = int(input('enter alcohol :'))
    alcohol.append(z)

alcohol = np.array(alcohol).reshape(-1,1)

print(c.predict(alcohol))







