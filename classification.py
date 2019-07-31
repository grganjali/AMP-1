from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn import preprocessing
from sklearn.metrics import classification_report, auc, roc_curve, confusion_matrix, matthews_corrcoef

import numpy as np
import ntpath
import pandas as pd
import sys

class MultiColumnLabelEncoder(preprocessing.LabelEncoder):
    def __init__(self,columns=None):
        self.columns = columns

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = preprocessing.LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = preprocessing.LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)

def main():
    dataset = sys.argv[1]
    target = sys.argv[2]
    output_folder = sys.argv[3]
    identifier = ntpath.basename(dataset)

    # TODO REMOVE ALL OTHER TARGET CLASSES
    df = pd.read_csv(dataset, sep=',', quotechar='\'')
    all_columns = df.columns
    numeric_columns = df._get_numeric_data().columns
    categorical_columns = list(set(all_columns)-set(numeric_columns))
    data = MultiColumnLabelEncoder(columns=categorical_columns).fit_transform(df)

    columns = ['IIRLM2','SBHF','IIP43sign','IIIP51sign','VIEMRatio25','IIHIAsign','V6Rsign']
    y = data[target]
    #X = data.drop(target, axis=1)
    X = data[columns]
    clf = RandomForestClassifier(n_estimators=100,random_state=0,n_jobs=-1)
    y_pred = cross_val_predict(clf, X, y, cv=10)
    report = classification_report(y,y_pred)
    print(confusion_matrix(y,y_pred))
    print(pd.DataFrame(confusion_matrix(y, y_pred, labels=[1,0]), index=['true:1', 'true:0'], columns=['pred:1', 'pred:0']))
    print(report)
    fpr, tpr, thresholds = roc_curve(y, y_pred)
    print("FPR")
    print(fpr)
    print("TPR")
    print(tpr)
    auc_score = round(auc(fpr, tpr),2)
    print(auc_score)
    mcc = matthews_corrcoef(y,y_pred)
    print("MCC")
    print(mcc)

    parsed_report = report.strip().split("\n")
    output_list = list()

    for i in [2,3]:
        metrics = parsed_report[i].split()
        output_list.append({
            'class':metrics[0],
            'precision':metrics[1],
            'recall':metrics[2],
            'f1_score':metrics[3],
            'auc':auc_score,
            'mcc':mcc,
        })

    df_output = pd.DataFrame(output_list)
    df_output.to_csv(output_folder + "/" + identifier + "_performance.csv", index=False)
    return True

if __name__ == "__main__":
    main()
