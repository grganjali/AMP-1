import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
# #print(iris_dataset['DESCR'][:193] + "\n...")
# print(iris_dataset['target'][:200] )
# print(iris_dataset['target_names'][:200] )
# print(iris_dataset['feature_names'][:200] )
# print("type of data: {}".format(type(iris_dataset["data"])))
# print("shape of data: {}".format(iris_dataset["data"].shape))
# print("some first rows of the datafile: \n{}".format(iris_dataset["data"][:10]))
# print("target data type: {}".format(type(iris_dataset["target"])))
# print("target values:  \n{}".format(iris_dataset["target"]))

#
X_train,X_test, y_train,y_test= train_test_split(iris_dataset['data'], iris_dataset["target"], random_state=0)
print("X_train shape; {}".format(X_train.shape))
print("y_train shape; {}".format(y_train.shape))
print("X_test shape; {}".format(X_test.shape))
print("y_test shape; {}".format(y_test.shape))

iris_dataframe= pd.DataFrame(X_train, columns=iris_dataset.feature_names)

print("iris_dataframe: \n{}". format(iris_dataframe[:5]))
# pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o', hist_kwds={'bins': 20}, s=60, alpha= 0.8, cmap= mglearn.cm3)
#
# knn=KNeighborsClassifier(n_neighbors=2)
# knn.fit(X_train, y_train)
#
# X_new=np.array([[5, 2.9, 1, 0.2]])
# print("X_new shape: {}".format(X_new.shape))
#
# # prediction= knn.predict(X_new)
# # print("prediction: {}".format(prediction))
# # print("predicted lable/target name: {}".format(iris_dataset["target_names"][prediction]))
#
# y_pred= knn.predict(X_test)
# print("Test set predicions: {}".format(y_pred))
#
# print("Test score using mean: {:.2f}".format(np.mean(y_pred==y_test)))
# print("Test score using score method: {:.2f}".format(knn.score(X_test, y_test)))
