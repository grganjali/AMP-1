from Bio import SeqIO
from Bio.Seq import Seq
from os.path import join
import pandas as pd


path= "/home/anjali/06/datasets/output70.out"

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
Qfasta.to_csv(path_or_buf='datasets/cdhit70.csv')
