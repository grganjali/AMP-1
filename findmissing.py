import pandas as pd

features_file= pd.read_csv("/home/anjali/06/datasets/features.csv")
sequence_file= pd.read_csv("/home/anjali/06/datasets/sequence.csv")

features_seq= list(features_file.seq)
sequence_seq= list(sequence_file.sequence)

# print(list(features_seq))
missing= set(sequence_seq)-set(features_seq)
print(missing)
