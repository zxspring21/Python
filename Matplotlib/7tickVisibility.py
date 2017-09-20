import matplotlib.pyplot as plt
import numpy as np
#Our goal is show the axial value when the line overlap the value and
#let the value become transparent for available to see the value.

x= np.linspace(-3,3,50)
y = 0.1*x
plt.figure()
plt.plot(x,y,linewidth = 10)
plt.ylim(-2,2)

#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position( ('data',0) )
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# bbox= background boundingbox ,alpha = transparency
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor= 'None',alpha=0.7))
  

plt.show()
print('We cannot accomplish the goal until we find the bugs in the result.')
