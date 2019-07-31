import csv
import pandas as pd
from ast import literal_eval

features_file= pd.read_csv("/home/local/BHRI/agarg/06/datasets/features.csv")
features_membpos= pd.read_csv("/home/local/BHRI/agarg/06/datasets/membpos.csv", sep=",")

subcol_names= ['R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U', 'G',
            'P', 'A', 'V', 'I', 'L', "M", "F", "Y", "W"]
keys= features_membpos.keys()

N_values= features_membpos.Nterminal
col_names= ['N_R', 'N_H', 'N_K', 'N_D', 'N_E', 'N_S', 'N_T', 'N_N', 'N_Q', 'N_C', 'N_U', 'N_G',
            'N_P', 'N_A', 'N_V', 'N_I', 'N_L', "N_M", "N_F", "N_Y", "N_W"]
N_df= pd.DataFrame(columns= col_names)
for item in range(len(N_values)):
    val= literal_eval(N_values[item])
    for c1, c2 in zip(subcol_names, col_names):
        val[c2]= val.pop(c1)
#     print(val)
    N_df= N_df.append(val, ignore_index= True)


C_values= features_membpos.Cterminal
col_names= ['C_R', 'C_H', 'C_K', 'C_D', 'C_E', 'C_S', 'C_T', 'C_N', 'C_Q', 'C_C', 'C_U', 'C_G',
            'C_P', 'C_A', 'C_V', 'C_I', 'C_L', "C_M", "C_F", "C_Y", "C_W"]
C_df= pd.DataFrame(columns= col_names)
for item in range(len(C_values)):
    val= literal_eval(C_values[item])
    for c1, c2 in zip(subcol_names, col_names):
        val[c2]= val.pop(c1)
    # print(val)
    C_df= C_df.append(val, ignore_index= True)

final_df= pd.concat([features_membpos, N_df, C_df], ignore_index= True, sort= False)
final_df.to_csv("/home/local/BHRI/agarg/06/datasets/membpos.csv", sep= ",")
