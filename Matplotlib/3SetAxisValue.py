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
"""
plt.yticks([-2,-1.8,-1,1.22,3,],
           ['really bad','bad','normal','good','really good'])
"""

print('We turned font into intalics,if there are spaces in sentence,we need ',
      'add conversion symbol \ which can show special symbols.')
plt.yticks([-2,-1.8,-1,1.22,3,],
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
plt.show()
