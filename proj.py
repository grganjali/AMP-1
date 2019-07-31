from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_alphabet

for seq_record in SeqIO.parse("lamp.fasta", "fasta"):
    # print(seq_record)
    print(repr(seq_record.seq))
    # print(seq_record)
    print("\n")
