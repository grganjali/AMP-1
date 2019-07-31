from Bio import SeqIO
from Bio.Seq import Seq

# fname= open("non-avp.fasta")
# newfile= open("n_avp.fasta", "a+")
#
# for line in fname:
#     array= line.split()
#     newfile.write(">{} \n{} \n".format(array[0], array[1]))
#     continue
#
# import glob
#
# read_files= glob.glob("non-avp*.txt")


fh= open("aps.fasta")
for seq_record in SeqIO.parse(fh, "fasta"):
     if "Predicted" not in seq_record.description.split('|'):
        print(seq_record)
