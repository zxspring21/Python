import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)

y1= 2*x+1
y2= x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
#modify x axis spacing 
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3,],
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
#gca = 'get current axis'
ax = plt.gca()
print('spines are four edges of the figure')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

print('y bind in 0 position')
#It also has outward,axes(position in percentage,show like 0.1=>10%)
ax.spines['bottom'].set_position( ('data',0) )

print('x bind in 0 position')
ax.spines['left'].set_position(('data',0))

plt.show()
