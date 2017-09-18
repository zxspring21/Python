import numpy as np
#pointer copy
a = np.arange(4)
print(a)
b=a
c=a
d=b
a[0] = 0.3
print(a)
print(b)
a[0] = 11
print(a)
print(b)
print(d is a)
d[1:3]=[22,33]
print(a)

#just copy value, it doesn't have correlation with a 
b = a.copy() #deep copy
print(b)
a[3] = 44
print('a=',a)
print('b=',b)
