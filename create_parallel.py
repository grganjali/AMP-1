import pandas as pd
df= pd.read_csv("datasets/cdhit70.csv")
sequences= df.sequence
l= len(sequences)

txtfile= open("file_parallel_cdhit.txt", "a+")

for seq, num in zip(sequences, range(l)):
    txtfile.write("python3 test4.py {} {}\n".format(seq, num+1))
