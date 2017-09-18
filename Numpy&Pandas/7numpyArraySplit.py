import numpy as np
A = np.arange(12).reshape(3,4)
print('A=',A)
print('A split vertical=\n',np.split(A,2,axis=1)) #split vertical
print('A split horizontal=\n',np.split(A,3,axis=0)) #split horizontal

print('A split vertically 3 sections nonequally=\n',np.array_split(A,3,axis=1)) # nonequal length split
# mark
print('A split horizontally 3 sections=\n',np.vsplit(A,3)) # horizontally split 3 sections
print('A split vertically 2 sections=\n',np.hsplit(A,2)) # vertically split two sections
