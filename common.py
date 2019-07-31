import pandas as pd

file_cdhit= "/home/anjali/06/datasets/cdhit70.csv"
file_sequence= "/home/anjali/06/datasets/sequence.csv"

df_cdhit= pd.read_csv(file_cdhit)
df_sequence= pd.read_csv(file_sequence)

print(len(df_cdhit.sequence))
print(len(set(df_cdhit.sequence).intersection(df_sequence.sequence)))
