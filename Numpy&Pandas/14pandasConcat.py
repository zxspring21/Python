import pandas as pd
import numpy as np


#concatenating
df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['a','b','c','d'])
print('df1=\n',df1,'\ndf2=\n',df2,'\ndf3=\n',df3)

res = pd.concat([df1,df2,df3],axis= 0)
print('\nconcat df1~df3=\n',res)
res2 = pd.concat([df1,df2,df3],axis= 0,ignore_index = True)
print('\nconcat df1~df3 sort by index=\n',res2)

#join,['inner','outer']
df4 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'],
                   index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1, columns = ['b','c','d','e'],
                   index=[2,3,4])
print('************')
print('origin df4=\n',df4,'\norigin df5=\n',df5)

res3 = pd.concat([df4,df5])
print('concat df4~df5 if not assign join property',
      'then system will choose outer=\n',res3)

res4 = pd.concat([df4,df5],join = 'outer')
print('concat outer which means to integrate all values in new DataFrame',
      ',and some values which cannot match the index will show nan',
      'in df4~df5=\n',res4)
res5 = pd.concat([df4,df5],join = 'inner')
print('concat inner which choose',
      'the same sections df4~df5=\n',res5)
res6 = pd.concat([df4,df5],join = 'inner',ignore_index =True)
print('concat inner which choose',
      'the same sections and sort by order df4~df5=\n',res6)
res7 = pd.concat([df4,df5],axis=1,join_axes=[df4.index])
print(res7)

res8 = pd.concat([df4,df5],axis=1)
print(res8)

#append
print('***append****')
df10 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'])
df11 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
df12 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
#res10 = df10.append(df11,ignore_index = True)
res10 = df10.append([df11,df12],ignore_index = True)

print('append horizontally df10 to df11:\n ',res10)
s1 = pd.Series([1,2,3,4],index = ['a','b','c','d'])
res11 = df10.append(s1,ignore_index=True)
print('append Series into df10:\n',res11)


