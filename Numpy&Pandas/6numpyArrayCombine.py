import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack( (A,B) ) #vertical stack, horizontal hstack
print(C) 
print(A.shape,C.shape)
print(A[np.newaxis,:])
print(A[:,np.newaxis])
print(A[:,np.newaxis].shape)

D = np.array([1,1,1])[:,np.newaxis]
E = np.array([2,2,2])[:,np.newaxis]
F = np.hstack( (D,E,D) )
print('D=',D,'\nE=',E,'\nF=',F)

G = np.concatenate((D,E,E,D),axis=0)
H = np.concatenate((D,E,E,D),axis=1)
# multiarray combine,0=updown,1=leftright
print('G=',G,'\nH=',H)
