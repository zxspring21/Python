
from sklearn import datasets
from sklearn import svm
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data,iris.target
clf.fit(X,y)

#method 1 pickle which can store value
#it must create save_folder first,otherwise it will get error.
#save
with open('save/clf.pickle','wb') as f:
    pickle.dump(clf,f)

"""
iris = datasets.load_iris()
X,y = iris.data,iris.target
#restore
with open('save/clf.pickle','rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))
#Result will show [0],it can represent prediction success.
"""
#method 2 :joblib which store/load action more fast than pickle
from sklearn.externals import joblib
#Save
joblib.dump(clf,'save/clf.pkl')
#restore
clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))

#You want to save predictable model to other application
#if you don't save these training data, it wastes time a lot.
#if you want to predict something, but you need to wait 30 or more time
#it isn't a good solution.
#So saving the model,if you want to predict something
#you can directly use the model!
