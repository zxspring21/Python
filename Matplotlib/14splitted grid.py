import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1:subplot2grid
#******************************************
"""
plt.figure()
#3 rows,3 columns,index from (0,0)
ax1 = plt.subplot2grid( (3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
#if the front of section is axis,we need to use set_title
#else if it is figure,then we need title()
ax2 = plt.subplot2grid( (3,3),(1,0),colspan=2,)
ax3 = plt.subplot2grid( (3,3),(1,2),rowspan=2,)
ax4 = plt.subplot2grid( (3,3),(2,0))
ax4 = plt.subplot2grid( (3,3),(2,1))
"""
#******************************************
#method 2:gridspec
"""
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])
"""
#******************************************
#method 3:easy to define structure
f,( (ax11,ax12),
    (ax21,ax22) )=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
#2 rows,2 columns,not subplot,f just parameter which can judge

#******************************************
plt.tight_layout()
plt.show()
