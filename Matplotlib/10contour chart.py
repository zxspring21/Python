import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    #compute the contour height function
    return (1-x/3+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
#use plt.contourf to filling contours
# x,y and value for(x,y)point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#give a value to corresponding cmap(color map) to represent a color
# 8 is represented 10 sections, 0->let the picture split 2 sections

#use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
#adding label
plt.clabel(C,inline=True,fontsize=10)
#Choosing True would draw words in line,False will let the words across line. 

#remove the picture of ticks
plt.xticks(())
plt.yticks(())
plt.show()
