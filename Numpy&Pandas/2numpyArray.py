import numpy as np
def main():
    a = np.array([ [2,32,3],
                   [2,33,4]],dtype = np.int) #int=int64,also has int32,float64,float32.
    b = np.zeros((3,4))
    c = np.ones((3,4),dtype = np.int16)
    d = np.empty((3,4))  #converge to 0
    e = np.arange(10,20,2)  #sort array similar to range
    f = np.arange(12).reshape((3,4))
    g = np.linspace(1,10,20)
    h = np.linspace(1,10,6).reshape((2,3))
    print(a.dtype)
    print('a=',a,'\nb=',b,'\nc=',c,'\nd=',d)
    print('e=',e,'\nf=',f,'\ng=',g,'\nh=',h)
if __name__ == '__main__':
    main()
