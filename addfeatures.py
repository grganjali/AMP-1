import csv
import pandas as pd

file_seq= "/home/anjali/06/datasets/sequence.csv"
file_features= "/home/anjali/06/datasets/features.csv"

# fh_seq= open(file,seq, "r")

seq_info= pd.read_csv(file_seq)
features_info= pd.read_csv(file_features)


num = [[seq,db] for [seq,db] in zip(seq_info.sequence,seq_info.Database) if db=="APD3"]
print(len(num))

s=list()
for item in num:
    s.append(num[0])

df= seq_info
df2= features_info
df_apd3=dict()
df_apd3.update(df)
df_apd3.update(df2)

# df_apd3.append(f for f in features_info.sequence if f in s)
#
# for f in features_info.sequence:
#     if(f in s):
#         print(f)

f=list()
f=features_info.sequence
# print(len(features_info.sequence))

print(len(f))

for item in f:
    for seq in s:
        if(item==seq):
            d=d.update


# # if(seq_info.Database=="APD3"):
# #     df=dict()
# #     df["sequence"]=seq_info.sequence
#
# # d=dict()
# # d["sequence"]["Database"]= [[seq,db] for [seq,db] in zip(seq_info.sequence,seq_info.Database) if db=="APD3"]
#
#
# # for f,s in zip(features_info.sequence, num):
# #     # print(f)
# #     # print(s[1])
# #     if(f==s[0]):
# #         print(f)
#         # df_apd3.update({"sequence": "f"})
#
# # print(len(df_apd3["sequence"]))
# seq= list()
# for item in num:
#     seq.append(item[0])
#
# print(seq[0])
#
# d=dict()
# d2=dict()
# for f in features_info.sequence:
#     if(f in seq):
#         d["sequence"]= f
#         d2.append(d)
