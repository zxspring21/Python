import numpy as np
def main():
    
    A = np.arange(2,14).reshape((3,4))
    print(A)
    print('A min=',np.argmin(A))
    print('A max=',np.argmax(A))
    print('A mean=',np.mean(A)) # the same as A.mean(),np.average(A)
    print('A median=',np.median(A)) 
    print('A plus step by step=',np.cumsum(A)) #step plus
    print('A difference step by step=',np.diff(A))
    print('A find nonzero=',np.nonzero(A)) # print two array nonzero item
    B = np.arange(14,2,-1).reshape((3,4))
    print('B =',B)
    print('B sort raw by raw=',np.sort(B))
    print('B transpose=',np.transpose(B)) # the same as B.T
    print('B matrix multiplication=',(B.T).dot(B)) #matrix multiplication
    print('B <5 will =5,>9 will=9,else stay origin=',np.clip(B,5,9))

    #axis=1 raw, axis=0,column
    print(np.mean(B,axis=1))

if __name__ == '__main__':
    main()
