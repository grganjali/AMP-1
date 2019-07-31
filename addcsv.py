import csv
from os import listdir
from os.path import isfile, join
import pickle
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


file_list= listdir("/data/outputs_cdhit")

file_list.sort(key=natural_keys)
# print("out1.txt" in file_list)
files= [join("/data/outputs_cdhit", f) for f in file_list]
# print("/data/outputs/out15645.txt" in files)

features= ['seq', 'Tiny', 'Small', 'Aliphatic', 'Aromatic', 'NonPolar', 'Polar', 'Charged', 'Basic', 'Acidic', 'aindex', 'autocovariance', 'autocorrelation', 'BLOSUM1', 'BLOSUM2', 'BLOSUM3', 'BLOSUM4', 'BLOSUM5', 'BLOSUM6', 'BLOSUM7', 'BLOSUM8', 'BLOSUM9', 'BLOSUM10', 'boman', 'charge', 'crosscovariance', 'PP1', 'PP2', 'PP3', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'hmoment', 'hydrophobicity', 'instaindex', 'KF1', 'KF2', 'KF3', 'KF4', 'KF5', 'KF6', 'KF7', 'KF8', 'KF9', 'KF10', 'lengthpep', 'MSWHIM1', 'MSWHIM2', 'MSWHIM3', 'mw', 'pI', 'ProtFP1', 'ProtFP2', 'ProtFP3', 'ProtFP4', 'ProtFP5', 'ProtFP6', 'ProtFP7', 'ProtFP8', 'ST1', 'ST2', 'ST3', 'ST4', 'ST5', 'ST6', 'ST7', 'ST8', 'T1', 'T2', 'T3', 'T4', 'T5', 'VHSE1', 'VHSE2', 'VHSE3', 'VHSE4', 'VHSE5', 'VHSE6', 'VHSE7', 'VHSE8', 'Z1', 'Z2', 'Z3', 'Z4', 'Z5']

csvdir="/home/anjali/06/datasets"
fcsv= "cdhit_features.csv"

with open (join(csvdir, fcsv), mode="w") as csv_file:
    fieldnames= features
    writer= csv.DictWriter(csv_file, fieldnames= fieldnames, extrasaction= "ignore")
    writer.writeheader()
    for file in files:
        fh= open(file, "rb")
        info= pickle.load(fh)
        writer.writerow(info)
    # fh= open(files[0], "rb")
    # info= pickle.load(fh)
    # writer.writerow(info)
