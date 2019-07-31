from Bio import SeqIO

file=open("datasets/sample.fasta")

for seq_record in SeqIO.parse(file, "fasta"):
    print(seq_record)
