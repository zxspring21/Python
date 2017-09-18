import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods= 6)
df =pd.DataFrame(np.arange(24).reshape(6,4),
                 index = dates,columns=['A','B','C','D'])
print('df = \n',df)
print('**********')
print(dates)
print(df['A'],'\n',df.A) # the same result
print(df[0:3],df['20130102':'20130104'])
#select by label: loc
print('**********')
print(df.loc['20130102'])
print('select in all rows and A,B columns : ',df.loc[:,['A','B']])
print('select in perticular position : ',df.loc['20130102',['A','B']])

#selected by position: iloc
print(df.iloc)
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])

#mixed index with selection: ix
print(df.ix[:3,['A','C']])

#Boolean indexing
print(df[df.A > 8])


