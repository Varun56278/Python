#Question : 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.DataFrame()
print(data)

d ={'eid':[11,222,444,555,1,2,3], 
    'ename':['Sumit','harry','Divya','hritik','shubham','Shilpa','priya'],
    'edeparment':['Engineering','Medical','Sale','Management','Electric','Labour','CRM'],
    'gender':['male','male','female','male','male','female','female'],
    'age':[23,25,24,27,21,23,30]}

HR = pd.DataFrame(data=d,index=['a','b','c','d','e','f','g'])
print(HR)

#HR.to_csv('HR.csv',index=False)


#Question : 3
print(HR[['edeparment','age']])

#Question : 4
salary = ['89000','45000','19000','72000','130000','53000','89000']

HR['salary'] = salary
print(HR)

#grouping
g = HR.groupby('salary')
print(g)


for salary, salary_HR in g:
    print(salary)
    print(salary_HR)

u  = HR.groupby(["age", "gender"]).count()
print(u)

#loc
t = HR.loc[['a','b','c']]
print(t)

u = HR.loc[['a','b','c'],['salary']]
print(u)

#iloc
h = HR.iloc[0]
print(h)





#Question : 5
sns.barplot(x = 'edeparment',y = 'age', data=HR)
plt.show()


sns.barplot(x = 'age', data=HR)
plt.show()



#question : 2
NaN is the default missing value marker in pandas
NaN is ceate default by over speed and convenience.
Detect all missing value in a DataFrame with different types: str,list ,boolean and blank space etc
