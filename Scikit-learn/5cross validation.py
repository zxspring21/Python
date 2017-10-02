from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


iris = load_iris()
X = iris.data
y = iris.target

"""
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
#use this func to train , we get 5 neighbors to predict y
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)
#y_pred = knn_predict(X_test)

#we use test_data to test score rate
print(knn.score(X_test,y_test))

"""

#We want to split 5 sets test datas
"""
#Then we will get non-equal test and training data and get the average value.
#To let the result more accurate.

knn = KNeighborsClassifier(n_neighbors = 5)
scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy') # split 5 sections
print(scores)
print('average value:',scores.mean())

"""
#so how to choose parameter?
#classification or regression problem

k_range = range(1,31)
k_scores= []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    #for classification
    """
    scores = cross_val_score(knn, X,y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
    """
    #for regression,and add minus symbol
    loss = -cross_val_score(knn, X,y, cv=10, scoring='mean_squared_error')
    k_scores.append(loss.mean())
    #we can choose k=13~18 parameter, or change knn model,
    #then we will get better result.

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
