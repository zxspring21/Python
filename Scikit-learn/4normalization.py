from sklearn import preprocessing
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

#normalization = scale
#if the value range too big, then the result is hard to converge to local minimum
#or global minimum

a = np.array([[10,2.7,3.6],
              [-100,5,-2 ],
              [120,20,40 ]],dtype=np.float64)


print('origin value:\n',a)
print('after nomalization:\n',preprocessing.scale(a))
#it's better for machine learning data processing architecture.

X, y = make_classification(n_samples=300, n_features=2, n_redundant=0,
                           n_informative=2,random_state=22,
                           n_clusters_per_class=1,scale=100)
"""
plt.scatter(X[:,0],X[:,1],c=y)
# y represent[1 1 1 1 0 0 0 1...] array ,we can think c=y equal to c= 'color'
plt.show()
"""

#X = preprocessing.minmax_scale(X,feature_range=(0,1))
X = preprocessing.scale(X)
#if we don't have scale this step, the score will 0.9->0.5.
#it's not a good result.

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3)
clf = SVC()
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
