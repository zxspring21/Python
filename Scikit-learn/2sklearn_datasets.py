from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target #label

model = LinearRegression()
#There are many parameter which can be used
#We don't need normalization...steps
#to optimize the data now.
model.fit(data_X,data_y)

print('predict:\n',model.predict(data_X[:4,:]))
print('actual:\n',data_y[:4])

X,y = datasets.make_regression(n_samples=100,n_features=1,
                               n_targets=1,noise=1)
#We can add noise value to let the datasets in a mess

plt.scatter(X,y)
plt.show()
