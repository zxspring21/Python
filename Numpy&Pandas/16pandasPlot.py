import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plot data

#Series
data = pd.Series(np.random.randn(1000),index = np.arange(1000))
data = data.cumsum() #accumulate
"""
data.plot()
plt.show()
"""
#DataFrame
data2 = pd.DataFrame(np.random.randn(1000,4),
                    index = np.arange(1000),
                    columns = list("ABCD") )
data2 = data2.cumsum()
print(data2.head(3)) #data.head(),default option is 5

#plot methods:
# 'bar','hist','box','kde','area','scatter','hexbin','pie'
#below code will show  A,B column data as data point.
print('show  A,B column data as data point.')
ax = data2.plot.scatter(x='A',y='B',color='DarkBlue',label ='Class 1')
data2.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)

plt.show()
