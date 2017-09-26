import matploblib as plt
import numpy as np
#image data
a = np.array([0.3136608,0.3653484,0.42373312,0.3653484184,0.439599993,
              0.5250837,0.42373312013,0.52508375,0.6515363513]).reshape(3,3)

"""
interpolation example:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
"""
plt.imshow(a,interpolation= 'nearest',cmap='bone',origin='upper')#cmap=plt.cm.bone
plt.colorbar(shrink=0.9)
plt.xticks(())
plt.yticks(())
plt.show()
