import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor 


data = pd.read_csv('Card.csv') 
print(data)
x = data.iloc[:, 1:2].values  
print(x) 
y = data.iloc[:, 2].values
print(y)



  
x = np.array(x).reshape(-1,1)
print(x)

tree = RandomForestRegressor(n_estimators = 100, random_state = 0) 

c = tree.fit(x,y)
print(c)


b = c.predict(x)
print(b)

  
 
X_grid = np.arange(min(x), max(x))  
  
                  
X_grid = np.array(x).reshape(-1,1)
  
 
plt.scatter(x, y, color = 'blue')   
  
 
plt.plot(X_grid, c.predict(X_grid),  
         color = 'green')  
plt.title('Random Forest Regression') 
plt.xlabel('Position level') 
plt.ylabel('Salary') 
plt.show()
