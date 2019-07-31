from from_fasta import from_fasta
from from_camp import from_camp
from from_txt import from_txt
from Bio import SeqIO

if input("from fasta? ") == "yes":
    fasta_handle= from_fasta()

if input("from camp? ") == "yes":
    camp_handle= from_camp()

if input("from text? ") == "yes":
    txt_handle= from_txt()
    # for seq_record in SeqIO.parse(txt_handle, "fasta"):
    #     print(seq_record)
