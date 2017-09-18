import pandas as pd
import numpy as np
#numpy -> list, pandas -> dict
s = pd.Series([1,3,6,np.nan,44,1]) # nan -> none
print(s)
dates =pd.date_range('20170915',periods = 6)
print(dates)
#row = index , column =columns
# use numpy to guide to pandas data format
df=pd.DataFrame(np.random.randn(6,4),index =dates,columns=['a','b','c','d'])

print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print(df2)
print(df2.dtypes)
print(df2.index) #columns
print(df2.columns) #raw
print(df2.values)
#it just computes numbers count,for example, mean, std, min,..
print(df2.describe())
print(df2.T)# transpose
print(df2.sort_index(axis=1,ascending=False)) # axis=0,horizontal,axis=1,vertical

print(df2.sort_values(by='E')) #sort by words count
