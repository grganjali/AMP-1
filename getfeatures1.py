import csv
import pandas as pd
from ast import literal_eval

features_file= pd.read_csv("/home/anjali/06/datasets/features.csv")


tiny_values=features_file.Tiny
col_names= ['tiny_number', "tiny_percentage"]
tiny_df = pd.DataFrame(columns= col_names)
#Getting out tiny values for sequences:
for item in range(len(tiny_values)):
    val=features_file.Tiny[item]
    df= literal_eval(val)
    # print(df)
    tiny_df= tiny_df.append({"tiny_number":"{}".format(df["number"]), "tiny_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_tiny_number"]= tiny_df["tiny_number"]
features_file["column_tiny_percentage"]= tiny_df["tiny_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



Small_values=features_file.Small
col_names= ['Small_number', "Small_percentage"]
Small_df = pd.DataFrame(columns= col_names)
#Getting out Small values for sequences:
for item in range(len(Small_values)):
    val=features_file.Small[item]
    df= literal_eval(val)
    # print(df)
    Small_df= Small_df.append({"Small_number":"{}".format(df["number"]), "Small_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Small_number"]= Small_df["Small_number"]
features_file["column_Small_percentage"]= Small_df["Small_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



Aliphatic_values=features_file.Aliphatic
col_names= ['Aliphatic_number', "Aliphatic_percentage"]
Aliphatic_df = pd.DataFrame(columns= col_names)
#Getting out Aliphatic values for sequences:
for item in range(len(Aliphatic_values)):
    val=features_file.Aliphatic[item]
    df= literal_eval(val)
    # print(df)
    Aliphatic_df= Aliphatic_df.append({"Aliphatic_number":"{}".format(df["number"]), "Aliphatic_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Aliphatic_number"]= Aliphatic_df["Aliphatic_number"]
features_file["column_Aliphatic_percentage"]= Aliphatic_df["Aliphatic_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



Aromatic_values=features_file.Aromatic
col_names= ['Aromatic_number', "Aromatic_percentage"]
Aromatic_df = pd.DataFrame(columns= col_names)
#Getting out Aromatic values for sequences:
for item in range(len(Aromatic_values)):
    val=features_file.Aromatic[item]
    df= literal_eval(val)
    # print(df)
    Aromatic_df= Aromatic_df.append({"Aromatic_number":"{}".format(df["number"]), "Aromatic_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Aromatic_number"]= Aromatic_df["Aromatic_number"]
features_file["column_Aromatic_percentage"]= Aromatic_df["Aromatic_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



NonPolar_values=features_file.NonPolar
col_names= ['NonPolar_number', "NonPolar_percentage"]
NonPolar_df = pd.DataFrame(columns= col_names)
#Getting out NonPolar values for sequences:
for item in range(len(NonPolar_values)):
    val=features_file.NonPolar[item]
    df= literal_eval(val)
    # print(df)
    NonPolar_df= NonPolar_df.append({"NonPolar_number":"{}".format(df["number"]), "NonPolar_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_NonPolar_number"]= NonPolar_df["NonPolar_number"]
features_file["column_NonPolar_percentage"]= NonPolar_df["NonPolar_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")




Polar_values=features_file.Polar
col_names= ['Polar_number', "Polar_percentage"]
Polar_df = pd.DataFrame(columns= col_names)
#Getting out Polar values for sequences:
for item in range(len(Polar_values)):
    val=features_file.Polar[item]
    df= literal_eval(val)
    # print(df)
    Polar_df= Polar_df.append({"Polar_number":"{}".format(df["number"]), "Polar_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Polar_number"]= Polar_df["Polar_number"]
features_file["column_Polar_percentage"]= Polar_df["Polar_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



Charged_values=features_file.Charged
col_names= ['Charged_number', "Charged_percentage"]
Charged_df = pd.DataFrame(columns= col_names)
#Getting out Charged values for sequences:
for item in range(len(Charged_values)):
    val=features_file.Charged[item]
    df= literal_eval(val)
    # print(df)
    Charged_df= Charged_df.append({"Charged_number":"{}".format(df["number"]), "Charged_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Charged_number"]= Charged_df["Charged_number"]
features_file["column_Charged_percentage"]= Charged_df["Charged_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")





Basic_values=features_file.Basic
col_names= ['Basic_number', "Basic_percentage"]
Basic_df = pd.DataFrame(columns= col_names)
#Getting out Basic values for sequences:
for item in range(len(Basic_values)):
    val=features_file.Basic[item]
    df= literal_eval(val)
    # print(df)
    Basic_df= Basic_df.append({"Basic_number":"{}".format(df["number"]), "Basic_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Basic_number"]= Basic_df["Basic_number"]
features_file["column_Basic_percentage"]= Basic_df["Basic_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")



Acidic_values=features_file.Acidic
col_names= ['Acidic_number', "Acidic_percentage"]
Acidic_df = pd.DataFrame(columns= col_names)
#Getting out Acidic values for sequences:
for item in range(len(Acidic_values)):
    val=features_file.Acidic[item]
    df= literal_eval(val)
    # print(df)
    Acidic_df= Acidic_df.append({"Acidic_number":"{}".format(df["number"]), "Acidic_percentage": "{}".format(df["percentage"])}, ignore_index= True)
#get the last column name:
ncols= len(features_file.keys())
lastcol= features_file.keys()[ncols-1]
#add a column:
features_file["column_Acidic_number"]= Acidic_df["Acidic_number"]
features_file["column_Acidic_percentage"]= Acidic_df["Acidic_percentage"]
features_file.to_csv("/home/anjali/06/datasets/features.csv", sep=",")
