from Bio import SeqIO
from Bio.Seq import Seq
from from_fasta import from_fasta
from from_camp import from_camp
from from_txt import from_txt
from os.path import join
import pandas as pd

print("----------FASTA----------")
fasta_handle= from_fasta()
print("----------CAMP----------")
camp_handle= from_camp()
print("----------TEXT----------")
txt_handle= from_txt()
#
# fasta_handle= join(input("Directory: "), input("fastafile name: "))
# camp_handle= join(input("Directory: "), input("campfile name: "))
# txt_handle= join(input("Directory: "), input("txtfile name: "))
path=join(input("Directory of final fasta file: "), input("Final fasta file name: "))
file_fasta =open(path, "a+")


files= [fasta_handle, camp_handle, txt_handle]
# for file in files:
#     for seq_record in SeqIO.parse(file, "fasta"):
#         print(seq_record)

for file in files:
    for seq_record in SeqIO.parse(file,"fasta"):
        if seq_record.seq not in  SeqIO.to_dict(SeqIO.parse(file_fasta, "fasta"), key_function = lambda rec:rec.seq).keys():
            SeqIO.write(seq_record, file_fasta, "fasta")

# for seq_record in SeqIO.parse(file_fasta,"fasta"):
#     print(seq_record)

type=['Antibacterial', 'Antifungal', 'Antiviral', 'Antiparasitic']
with open(path) as fasta_file:
    identifiers = []
    sequence=[]
    pepClass=[]
    subclass=[]
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):  # (generator)
        identifiers.append(seq_record.id.split('|')[0])
        sequence.append(seq_record.seq)
        if "non-antimicrobial" in seq_record.id.split('|'):
            pepClass.append("NAMP")
        else:
            pepClass.append("AMP")
        if set(type).intersection(seq_record.id.split('|')):
            subclass.append(list(set(type).intersection(seq_record.id.split('|')))[0])
        else:
            subclass.append(' ')
s1 = pd.Series(identifiers, name='ID')
s2 = pd.Series(sequence, name='Sequence')
s3 = pd.Series(pepClass, name='pepClass')
s4 = pd.Series(subclass, name='Subclass')

#Gathering Series into a pandas DataFrame and rename index as ID column
Qfasta = pd.DataFrame(dict(ID=s1, sequence=s2, pepClass=s3, Subclass=s4 )).set_index(['ID'])
Qfasta.to_csv(path_or_buf='datasets/sequence.csv')
