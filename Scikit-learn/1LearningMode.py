import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#There are many datasets in sklearn. You can use it to any learning
#mode like Tensorflow to practice. classifier,regression...

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
#print(iris_X[:2,:])
#print(iris_y) #classification

X_train, X_test, y_train, y_test = train_test_split(iris_X,iris_y,
                                                    test_size=0.3)
#X_train+y_train -> 70%, X_test+y+test ->30%
#let the dataset out of order
print('dataset out of order:\n',y_train)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train) #training step
print('prediction value:\n',knn.predict(X_test))#use model property to predict classfication
print('Actual value:\n',y_test)
