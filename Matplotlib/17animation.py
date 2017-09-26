import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax =plt.subplots()

x = np.arange(0,2*np.pi, 0.01)
#,meaning return list,and choose the first position
line, = ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10)) #It can change i/100 to let the speed slowly.
    
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,

#animation = 100 frame,update 100 times, 20ms update once
#blit meaning is if update the graph all points(False),or when variation generation
#then update the variable points(True)

#func = animation , init_func = init
ani = animation.FuncAnimation(fig = fig, func = animate, frames=100,
                              init_func = init, interval=20,blit = False)

plt.show()
