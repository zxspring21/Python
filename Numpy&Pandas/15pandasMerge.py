import pandas as pd
#merging two df by key/keys. (may be used in database)
#simple example

print('*******merging two df by key/keys********')
left = pd.DataFrame({ 'key':['K0','K1','K2','K3'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3'],})

right = pd.DataFrame({ 'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3'],})

print('left=\n',left,'\nright=\n',right)
#res = pd.merge(left,right) This section also is the same result
res = pd.merge(left,right,on='key')
print('After merging left and right:\n',res)
print('********************')

print('******consider two keys*******')
#consider two keys
left2 = pd.DataFrame({ 'key1':['K0','K0','K1','K2'],
                       'key2':['K0','K1','K0','K1'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3'],})

right2 = pd.DataFrame({ 'key1':['K0','K1','K1','K2'],
                        'key2':['K0','K0','K0','K0'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3'],})

print('left2=\n',left2,'\nright2=\n',right2)
res2 = pd.merge(left2,right2,on=['key1','key2'])
print('After merging left2 and right2:\n',res2)
"""
Which represents the system default choice is inner,which merging
the same thing,
The final result seems like outer because
everything is in new dataFrame(X).
"""
print('********************')

print('******how = left,right,outer,inner********')
#how = ['left,'right','outer','inner']
#res3 = pd.merge(left2,right2,on=['key1','key2'])
#The result is the same as below codes
res4 = pd.merge(left2,right2,on=['key1','key2'],how= 'inner')
print('Choose how=inner,inner which represents the system default choice is inner',
      'which merging the same thing.\n',res4)
res5 = pd.merge(left2,right2,on=['key1','key2'],how= 'outer')
print('Choose how=outer,outer which means to integrate all values in new DataFrame',
      ',and some values which cannot match the index will show nan.\n',res5)
#how='right'. Based on right2 key1,key2 index choosing corresponing
#left2 members and values,if no corresponing members then will show nan.
res6 = pd.merge(left2,right2,on=['key1','key2'],how= 'right')
print('Choose how=right, Based on right2 key1,key2 index choosing corresponing',
      'left2 members and values,if no corresponing members then will show nan.\n',res6)
res7 = pd.merge(left2,right2,on=['key1','key2'],how= 'left')
print('Choose how=left',res7)

print('********************')

print('****indicator section*****')
#indicator
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']} )
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]} )
print('df1=\n',df1,'\ndf2=\n',df2)
res8 = pd.merge(df1,df2,on='col1',how='outer',indicator= True)
print('We choose indicator=True,but the default opion is False.\n',res8)
#give the indicater a custom name
res9 = pd.merge(df1,df2,on= 'col1',how='outer',indicator= "indicator_column")
print('Indicator =? can give the indicater a custom name\n',res9)


#merged by index
print('********************')
print('****merged by index*****')
left3 = pd.DataFrame({'A':['A0','A1','A2'],
                      'B':['B0','B1','B2']},
                      index = ['K0','K1','K2'])

right3 = pd.DataFrame({'C':['C0','C2','C3'],
                       'D':['D0','D2','D3']},
                       index = ['K0','K2','K3'])

print(left3)
print(right3)
#left_index and right_index default options are nan

res10 = pd.merge(left3,right3,left_index= True,right_index=True,how='outer')
res11 = pd.merge(left3,right3,left_index= True,right_index=True,how='inner')
print('left3,right3 merged by index outer:\n',res10)
print('left3,right3 merged by index inner:\n',res11)


#handle overlapping
print('********************')
print('****merged by index*****')
boys  = pd.DataFrame({'k' : ['K0','K1','K2'],'age':[1,2,3] })
girls = pd.DataFrame({'k' : ['K0','K0','K2'],'age':[4,5,6] })
print('boys:\n',boys)
print('girls:\n',girls)
res12 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print('boys and girls are merging innerly and renaming',
      'age as suffixes=[_boy,_girl] :\n',res12)

