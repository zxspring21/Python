import matplotlib.pyplot as plt

plt.figure()
"""
plt.subplot(2,2,1) # 2 rows,2 columns, draw picture in first place
#draw line from (0,0)->(1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2) # 2 rows,2 columns, draw picture in first place
plt.plot([0,1],[0,2])

plt.subplot(223) # 2 rows,2 columns, draw picture in first place
plt.plot([0,1],[0,3])

plt.subplot(224) # 2 rows,2 columns, draw picture in first place
plt.plot([0,1],[0,4])

"""
plt.subplot(2,1,1) #2 rows,1 columns
plt.plot([0,1],[0,1])

plt.subplot(2,3,4) #2 rows,3 columns,because we have 3 columns in this row
#so we need to accumulate previous columns account=3,and in this line first
#place,so 3+1=4
plt.plot([0,1],[0,2])

plt.subplot(235) # 3+2
plt.plot([0,1],[0,3])

plt.subplot(236) #3+3
plt.plot([0,1],[0,4])

plt.show()
