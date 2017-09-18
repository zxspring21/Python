class Fibb(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b =0,0,1
        print('self.max')
        print(self.max)
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<self.max:
            r = self.b
            self.a,self.b =self.b,self.a+self.b
            self.n = self.n +1
            return r
        raise StopIteration()
"""
def Fib(max):
    a,b=0,1
    while max:
        r=b
        a,b=b,a+b
        max-=1
        yield r
"""


def main():

    for i in Fibb(6):
        print(i)
if __name__ == '__main__':
    main()
