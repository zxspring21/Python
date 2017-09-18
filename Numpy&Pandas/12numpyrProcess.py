import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods= 6)
df =pd.DataFrame(np.arange(24).reshape(6,4),
                 index = dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print('origin=',df)
# deal with missing value, lose the value
# if change how ={'all'} , the row needed all nan numbers then lost the row 

#print(df.dropna(axis=0, how='any')) # if any none then lost

print('turn nan into 0 = \n',df.fillna(value=0))
print('if nan show false,else show true\n',df.isnull())
print('judge if any value = nan,if yes then return True\n',np.any( df.isnull() ) == True)

