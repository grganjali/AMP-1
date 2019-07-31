import pandas as pd
import subprocess
import sys

seq= list(pd.read_csv("/home/local/BHRI/agarg/06/datasets/features.csv")["seq"])
col_names= ["seq", "Nterminal", "Cterminal"]
subcol_names= ['R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U', 'G',
            'P', 'A', 'V', 'I', 'L', "M", "F", "Y", "W"]

df= pd.DataFrame(columns= col_names)
df["Nterminal"]= dict()
df["Cterminal"]= dict()


for item,i in zip(seq, range(len(seq))):

    output=  subprocess.check_output(["Rscript test3.R {} {}".format("membpos", item)], shell= True)
    output = output.decode().split("\n")
    output = [i for i in output if len(i) > 0]

    output_dict = dict()
    for i in range(3,len(output[3:])):
        values = output[i].split()
        output_dict[values[1]] = dict()
        output_dict[values[1]]['H'] = "{}".format(values[2])
        output_dict[values[1]]['uH'] = "{}".format(values[3])
        output_dict[values[1]]['MembPos'] = "{}".format(values[4])

    keys= list(output_dict.keys())
    l= len(keys)
    print(item, l)
    if l==0:
        continue
    N=dict()
    C=dict()

    for i in subcol_names:
        N.update({"{}".format(i): keys[0].count("{}".format(i))})

    for i in subcol_names:
        C.update({"{}".format(i): keys[l-1].count("{}".format(i))})

    # df.append([item, N, C], ignore_index= True)
    temp_dict= dict()
    temp_dict= {"sequence": item,
            "N": N,
            "C": C
    }
    # print(temp_dict)
    # temp_df= pd.DataFrame.from_dict(temp_dict)
    # df.append(temp_df, sort= False)
    # temp_df= pd.DataFrame([[item, N, C]], columns= col_names)
    df= df.append({"seq": item, "Nterminal": N, "Cterminal": C}, ignore_index=True)

print(df)
df.to_csv("/home/local/BHRI/agarg/06/datasets/membpos.csv", "\t")
