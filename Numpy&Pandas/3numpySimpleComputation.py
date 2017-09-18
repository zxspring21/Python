import numpy as np

def main():
    a = np.array([10,20,30,40])
    
    b = np.arange(4) #1-4
    print(a,b)
    c= a-b  #b^2 => b**2
    print(b**3)
    c = 10*np.sin(a) #tan,cos
    print(c)
    print('b=',b,'b<3',b<3) #b==3

    d = np.array([[1,2],[3,4]])
    e = np.arange(4).reshape((2,2))
    print('d=',d,'\ne=',e)
    print('0 represent sum of column d=',np.sum(d,axis=0))

    f = d*e # multiply one by one
    g = np.dot(d,e) #multiply two array, the same as a.dot(b)
    print('multiply d and e one by one=',d)
    print('d and e matrix multiplication=',e)

    h = np.random.random((2,4))
    
    print('h random matrix=',h)
    print('h sum=',np.sum(h))
    print('h represent sum of column h=',np.sum(h,axis=1))
    print('min=',np.min(h))
    print('max=',np.max(h))

if __name__ == '__main__':
    main()
