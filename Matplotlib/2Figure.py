import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)

y1= 2*x+1
y2= x**2
plt.figure()
plt.plot(x,y1)
print('********')
print('**use plt.figure() to split drawing picture***')

plt.figure(num=3, figsize=(8,5)) #length and width
plt.plot(x,y2)
#two '--' represent dotted line
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.show()
