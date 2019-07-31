#IMPORTING LIBRARIES AND DEPENDENCIES
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

from ipywidgets import widgets
import os
import plotly
plotly.tools.set_credentials_file(username='anjgrg98', api_key='j2GJ3FbQpYIbv8BcODz3')
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff
init_notebook_mode(connected=True)

import warnings
warnings.filterwarnings('ignore')


# DATA CURATION
data = pd.read_csv("/home/local/BHRI/agarg/06/datasets/cdhit_features.csv")
X=data.iloc[:, 1:97]
y= data.iloc[:, -2]

# X=np.nan_to_num(X)
# y=np.nan_to_num(y)

for col in X.keys():
    X[col].fillna(0, inplace=True)

y=pd.factorize(y)[0]

# FORWARD FEATURE SELECTION

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

rf_model= RandomForestClassifier(n_estimators= 1000, bootstrap= True, max_features= "sqrt")

cols= ["Feature", "Performance"]
performance=dict(columns= cols)

columns= [col for col in X.keys()]
for col in columns:
    X_try= X[col]
    X_train_ftry, X_test_ftry, y_train, y_test= train_test_split(X_try, y, random_state=0)
    rf_model.fit(X_train, y_train)
    y_pred= rf_model.predict(X_test_ftry)
    # performance.append(accuracy_score(y_test, y_pred))
    performance.update{col: accuracy_score(y_test, y_pred)}

sorted_perf= [(k,v) for (k,v) in sorted(performance.keys())]

train_cols=[ sorted_perf[0][0], sorted_perf[1][0]]
X_try= X[train_cols]

for i in range(len(X.keys)-1):
    for key in sorted_perf[:][0]:
        p"{}".format(i+3)= dict(columns= cols)
        train_cols.append(key)
        X_try=X[train_cols]
        X_train, X_test, y_train, y_test= train_test_split(X_try,y, random_state=0)
        rf_model.fit(X_train, y_train)
        y_pred= rf_model(X_test)
        P"{}".format(i+3).update({key: accuracy_score(y_test, y_pred)})
