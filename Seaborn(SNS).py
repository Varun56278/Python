import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('mn.csv')
print(df)

print(df.head())

print(df.corr())

sns.barplot(x = 'Sex',y = 'Survived', data=df)
plt.show()

sns.boxplot(x = 'Sex',y = 'Age',data= df ,palette= 'rainbow')
plt.show()

sns.boxplot(data=df ,palette= 'rainbow',orient='h')
plt.show()

sns.stripplot(x = 'Pclass',y = 'Fare', data=df)
plt.show()


sns.swarmplot(x = 'Pclass',y = 'Fare', data=df)
plt.show()


sns.swarmplot(x = 'Pclass',y = 'Fare',hue='Sex', data=df)
plt.show()

sns.heatmap(df.corr())
plt.show()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())

sns.heatmap(iris.corr())
plt.show()

sns.heatmap(iris.corr(), cmap= 'coolwarm',annot= True)
plt.show()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

sns.distplot(tips.total_bill)
plt.show()


sns.distplot(tips.total_bill,kde=False, bins=38)
plt.show()
