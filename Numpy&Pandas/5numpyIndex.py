import numpy as np
A = np.arange(3,15)
print(A)
print(A[3]) #0123
B = np.arange(3,15).reshape(3,4)
print(B)
print(B[2,1]) # B[2][1]
print(B[2,:])
print(B[:,1])
print(B[1,1:3])
for row in B:
    print(row)

for column in B.T:
    print(column)
print('transform B 3 raw,4col =>B 1 raw, value =\n',B.flatten()) 

for item in B.flat:    
    print(item) #print every item's value
