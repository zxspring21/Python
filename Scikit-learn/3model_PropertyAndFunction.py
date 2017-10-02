from sklearn import datasets
from sklearn.linear_model import LinearRegression
loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target #label

model = LinearRegression()
model.fit(data_X,data_y)

#print('predict:\n',model.predict(data_X[:4,:]))
#print('actual:\n',data_y[:4])
print(model.coef_) # y= 0.1x + 0.3 ,then coef: 0.1 , 0.3
print(model.intercept_)#y axis value intersect with model
print(model.get_params()) # get model which used parameters
print(model.score(data_X,data_y)) #score model,predict: data_X, result:data_y
#score actual value and predict value degree of matching
#which will show prediction success rate (Accuracy) =70%..
"""
If you use this dataset which classification model,
score criterion is R^2 coefficient of determination.
"""



