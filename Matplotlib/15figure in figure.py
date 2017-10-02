import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

#first graph
left,bottom,width,height = 0.1, 0.1, 0.8, 0.8

ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r') #RED
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

#second graph
left, bottom,width,height = 0.2,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b') #BLUE
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside1')

#another method
plt.axes([.6,0.2,0.25,0.25])
#x[startAt::endBefore:skip]
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside2')

#test

op = range(100)
for i in op[::-5]:
   print(i)

plt.show()
