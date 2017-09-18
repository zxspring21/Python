import threading
from time import time,localtime
import copy
"""import balance"""
class Calculator:
    
    name = 'Good Calculator'
    price = 18
    def __init__(self,name,height,weight):
        self.name =name
        self.h=height
        self.w=weight
        
       
    def add(self,a,b):
        print(self.name)
        print(a+b)
def inputfunc():
    
    try:
        file = open('eee.txt','r+')
    except Exception as e:
        print(e)
        answer = input('do you want to create a new file?')
        if answer == 'y':
            file = open('eee.txt','w')
        else:
            pass
    else:
        print('open file success')
        file.write('www')
        file.close()
    a = input('enter a number:')
    b =int(a)
    print('your number is = ',a)
    if b==1:
        print('this is 1')
    elif a=='hello':
        print('hey')
    else:
        print('what')
def dataFormat():
    tup = ('python',2.7,64)
    tuple2 = (1,2,3,4)
    tuple3 = 1,2,3,4
    a_list = [32.1,232,5555,12,4]
   
    for index in range(len(tuple2)):
       print("index = ",index,"number is =",tuple2[index])
    for index in range(len(a_list)):
       print("index = ",index,"number is =",a_list[index])

    a_list.append(0)
    a_list.insert(1,9)
    a_list.remove(12)
    print(a_list)
    a_list.append(0)
    print(a_list.count(0))
    a_list.sort()
    print(a_list)
    a_list.sort(reverse=True)
    print(a_list)
    
    d1 ={'apple':1,'pear':2,'orange':3}
    d2 ={1:'a',2:'b',4:'c'}
    print(d1['apple'])
    del d1['pear']
    print(d1)
    d1['b'] =20
    print(d1)
    print(d2[1])
    print(d2[2])
    print(d2[4])
    
    d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
    print(d4['pear'][3])    # a
    print(d4['orange'])

    
    multilist = [[1,2,3],[4,5,6],[7,8,9]]
    print(multilist[0][1])
    while True:
        b=input('input somesthing:')
        if b=='1':
           continue
        elif b=='2':
            break
        else:
            pass
        print('still in while' )
    print ('finish run')
    for i in tup:
        print(i)
    dic = {}
    dic['lan'] = 'python'
    dic['version'] =2.7
    dic['platform']=64
    for kr in dic:
        print(kr,dic[kr])
    s =set(['python','python2','python3','python4'])
    for item in s:
        print(item)
def func():
    return 0

def reportt(name,*grades):
    total_grade=0
    for grade in grades:
        print(grade)
        total_grade+=grade
    print(name,'total_grade=',total_grade)

def readwrite():
    text ='sjdfkjdslkfjlksdjfkl\nfsdkfjld'
    my_file =open('my file.txt','r')

    content = my_file.read()
    print(content)
    """my_file.write(text)"""
    """my_file.close()"""
    #zip lambda map
    a = [1,2,3]
    b =[4,5,6]
    ab = zip(a,b)
    print(ab)
    print(list(ab))

    for i,j in zip(a,b):
        print(i/2,j*2)
    #zip combine 
    fun = lambda x,y :x+y
    x =int(input('x='))
    y =int(input('y='))
    print(fun(x,y))
    #map combine func and parameter
    print(list(map(fun,[1],[2] )))
    print(list(map(fun,[1,2],[3,4])))
    #id copy 

    #copy -> pointer
    a = [1,2,[3,4],6]
    b =a #direct equal also pointer
    print('a',id(a))
    print('b',id(b))
    print(id(a)==id(b)) #pointer the same
    
    c =copy.copy(a) 
    print('c',id(c)) 
    print(id(a)==id(c))  #use copy ,just copy the value
    c[1] =22222
    print('a=',a,'c=',c)

    #deepcopy -> Not pointer 
    e =copy.deepcopy(a)
    a[2][0] = 3333
    print('a=',a,'e=',e) #use deepcopy ,just copy the value
    
    my_file.close()

def fun(x,y):
    return x+y
    
def main():
    "multiarray declare constructor"
    c = Calculator('bad calculator',1,3)
    print(c.name,c.h,c.w)
    """dataFormat()
    print(time.localtime())"""
    print(time())
    print(localtime())
    inputfunc()
    
    """reportt('Mike',1,3)"""
    readwrite()
    
    #pickle and set not read in foundation
if __name__== '__main__':
    main()
