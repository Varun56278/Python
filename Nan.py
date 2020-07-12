import pandas as pd
d = pd.read_csv('ss.csv',parse_dates=['datetime_utc'])
print(d.shape)
#print(d.head(10))
u = d.set_index('datetime_utc',inplace=True)
#print(u)


#k = d.isnull().tail()
#print(k)
#m = d.isnull().sum()
#print(m)
#h = d.dropna(how='all')
#print(h)


h = d.dropna()
print(h)
#new_d = d.fillna(0)
#print(new_d)

#den = d.fillna(method='bfill',axis='columns')
#print(den)

#den = d.fillna(method='ffill',limit=1)
#print(den)

#den = d.interpolate()
#print(den)
'''
den = d.replace({
     '_vism'       : 0,
     ' _windchillm': 4,
     '_heatindexm' : 'B'
     },np.NaN)
print(den)


den = d.fillna({
     '_vism'       : 0,
     ' _windchillm': 4,
     '_heatindexm' : 'B'
     })
print(den)
'''


#den.to_csv('den.csv',index=False)
