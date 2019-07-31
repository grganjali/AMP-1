from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import csv
import pandas

def from_camp():
    indir=input("directory name containing CAMP files: ")
    files = [join(indir,f) for f in listdir(indir) if isfile(join(indir, f))]

    outdir=input("directory of output fasta file: ")
    outfile= input("output fasta file name: ")
    path=join(outdir,outfile)
    file_fasta= open(path, "a+")

    n=0

    for file in files:
        dataframe = pandas.read_csv(file,delimiter="\t")
        # print(dataframe.keys())
        for index, row in dataframe.iterrows():
            # print("{} \t {}".format(index,row))
            if (row['Validation']!="Predicted") and (row['Seqence'] not in  SeqIO.to_dict(SeqIO.parse(file_fasta, "fasta"), key_function = lambda rec:rec.seq).keys()):
                file_fasta.write(">{}|{} \n {} \n".format(row['  Camp_ID'], row['Activity'], row['Seqence']))
                n=n+1
    print(n)
    return path


# print(dataframe['  Camp_ID'])
