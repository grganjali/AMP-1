from Bio.Seq import Seq
from Bio import SeqIO

file= "aps.fasta"

for seq_record in SeqIO.parse(file, "fasta"):
    print(seq_record.id)
    print(repr(seq_record))
    print(len(seq_record))
