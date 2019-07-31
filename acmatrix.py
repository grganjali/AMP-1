import pandas as pd
import matplotlib.pyplot as plt

seq_df= pd.read_csv("/home/anjali/06/datasets/features.csv")
df1= pd.DataFrame(seq_df)
# print(type(list(seq_df.keys())))
cols= [item for item in list(seq_df.keys()) if item not in ("Unnamed: 0", "seq")]
# print(cols)
features_df1= df1[cols]
# print(type(features_df))
# plt.figure()
plt.matshow(features_df1.corr())



apd3_df= pd.read_csv("/home/anjali/06/datasets/apd3.csv")
# print(apd3_df.keys())
unwanted=["ID", "seq", "Unnamed: 98", "pepClass", "Subclass", "Database", "Reference"]
df2= pd.DataFrame(apd3_df)
cols= [item for item in list(apd3_df.keys()) if item not in unwanted]
features_df2= df2[cols]
# plt.figure()
plt.matshow(features_df2.corr())


lamp_df= pd.read_csv("/home/anjali/06/datasets/lamp.csv")
# print(apd3_df.keys())
unwanted=["ID", "seq", "Unnamed: 98", "pepClass", "Subclass", "Database", "Reference"]
df3= pd.DataFrame(lamp_df)
cols= [item for item in list(lamp_df.keys()) if item not in unwanted]
features_df3= df3[cols]
# plt.figure()
plt.matshow(features_df3.corr())

plt.show()

corr
