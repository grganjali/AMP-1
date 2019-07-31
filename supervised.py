import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

datafile= pd.read_csv("/home/anjali/06/datasets/features.csv")

# print(datafile.keys())
y_cols= ["pepClass"]
x_cols= ['aindex', 'autocovariance', 'autocorrelation', 'BLOSUM1',
       'BLOSUM2', 'BLOSUM3', 'BLOSUM4', 'BLOSUM5', 'BLOSUM6', 'BLOSUM7',
       'BLOSUM8', 'BLOSUM9', 'BLOSUM10', 'boman', 'charge', 'crosscovariance',
       'PP1', 'PP2', 'PP3', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'hmoment',
       'hydrophobicity', 'instaindex', 'KF1', 'KF2', 'KF3', 'KF4', 'KF5',
       'KF6', 'KF7', 'KF8', 'KF9', 'KF10', 'lengthpep', 'MSWHIM1', 'MSWHIM2',
       'MSWHIM3', 'mw', 'pI', 'ProtFP1', 'ProtFP2', 'ProtFP3', 'ProtFP4',
       'ProtFP5', 'ProtFP6', 'ProtFP7', 'ProtFP8', 'ST1', 'ST2', 'ST3', 'ST4',
       'ST5', 'ST6', 'ST7', 'ST8', 'T1', 'T2', 'T3', 'T4', 'T5', 'VHSE1',
       'VHSE2', 'VHSE3', 'VHSE4', 'VHSE5', 'VHSE6', 'VHSE7', 'VHSE8', 'Z1',
       'Z2', 'Z3', 'Z4', 'Z5', 'column_tiny_number', 'column_tiny_percentage',
       'column_Small_number', 'column_Small_percentage',
       'column_Aliphatic_number', 'column_Aliphatic_percentage',
       'column_Aromatic_number', 'column_Aromatic_percentage',
       'column_NonPolar_number', 'column_NonPolar_percentage',
       'column_Polar_number', 'column_Polar_percentage',
       'column_Charged_number', 'column_Charged_percentage',
       'column_Basic_number', 'column_Basic_percentage',
       'column_Acidic_number', 'column_Acidic_percentage']
x_selected= ["column_Acidic_percentage", "PP3"]
X= datafile[x_selected].values
y= datafile[y_cols].values

X=np.nan_to_num(X)
y=np.nan_to_num(y)
y=y.ravel()


X_train, X_test, y_train, y_test= train_test_split(X,y,random_state=0)
clf=KNeighborsClassifier(n_neighbors=2)

clf.fit(X_train, y_train)

print("Test set prediction: {}".format(clf.predict(X_test)))
print("Test set accuracy: {:.2f}". format(clf.score(X_test, y_test)))


# knn visualisation

fig, axes= plt.subplots(1,3, figsize=(10,3))

for n_neighbors, ax in zip([1,3,9], axes):
    clf= KNeighborsClassifier(n_neighbors= n_neighbors).fit(X_train, y_train)
    mglearn.plots.plot_2d_separator(clf, X_train, fill=True, eps=0.5, ax=ax, alpha=0.4)
    # mglearn.discrete_scatter(X[0:10,0], X[0:10,1], y, ax= ax)
    ax.set_title("{} neighbors".format(n_neighbors))
    ax.set_xlabel("column_Acidic_percentage")
    ax.set_ylabel("PP3")
plt.show()
# ax[0].legend(loc=3)


# n_neighbors/accuracy

training_accuracy=[]
test_accuracy=[]

neighbors_setting= range(1,11)

for n_neighbors in neighbors_setting:
    clf= KNeighborsClassifier(n_neighbors= n_neighbors).fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbors_setting, training_accuracy, label= "training accuracy")
plt.plot(neighbors_setting, test_accuracy, label= "test accuracy")
plt.ylabel("accuracy")
plt.xlabel("n_neihbors")
plt.legend()
plt.show()
