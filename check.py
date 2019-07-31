from Bio import SeqIO

file= open("datasets/aps.fasta")

for seq_record in SeqIO.parse(file, "fasta"):
    print(seq_record.id)
    # print(SeqIO.to_dict(SeqIO.parse(file, "fasta"), key_function = lambda rec:rec.seq).keys())
