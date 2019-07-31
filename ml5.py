import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
from IPython.display import display
from sklearn.datasets import load_boston

boston= load_boston()
print("Feature names: {}".format(boston.feature_names))
print(boston['target_names'][:50] )


print("shape of the data: {}".format(boston.data.shape))

#feature engineering: Mixed features
X,y= mglearn.datasets.load_extended_boston()
print("X shape: {}".format(X.shape))
print("y shape: {}".format(y.shape))
# print("mixed features: \n{}".format(X[0][0:1]))
print("mixed features: \n{}".format(y[0]))
