from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio.Alphabet import generic_alphabet
from Bio.Alphabet import MutableSeq
from Bio.Seq import UnknownSeq

#PRINTING A SEQUENCE
my_seq= Seq("AGTACACTGGT")
my_seq

#Complement and reverse compliment
my_seq.complement()
my_seq.reverse_compliment()

#Parsing ls_orchid.fasta
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

#Parsing ls_orchid.gbk
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

#CREATING A SEQUENCE FROM GENERIC ALPHABET
my_seq= Seq("AGTACACTGGT")
my_seq
my_seq.alphabet

#Specify alphabet explicitly
my_seq=Seq("AGTACACTGGT". IUPAC.unambiguous_dna) #amino acid sequence: IUPAC.Protein
my_seq
my_seq.alphabet


#Sequence as strings
my_seq=Seq("GATCG", IUPAC.unambiguous_dna)
for index,letter in enumerate(my_seq):
    print("%i %s" %(index,letter))

#Accessing particular elements
print(my_seq[0])#first letter
print(my_seq[2])#third letter
print(my_seq[-1])#last letter

#NON-OVERLAPING-count
"AAAA".count("AA")
Seq("AAAA").count("AA")

#OVERLAPPING COUNT: to get GC%
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
len(my_seq)
my_seq.count("G")
100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq)

#Another method to calculate GC%
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
GC(my_seq)

#to concatenate heterogenous sequences: convert to generic alphabet:
protein_seq=Seq("EVRNAK", IUPAC.protein)
dna_seq=Seq("ACGT", IUPAC.unambiguous_dna)
protein_seq.alphabet= generic_alphabet
dna_seq.alphabet= generic_alphabet
protein_seq+dna_seq

#Make a sequence mutable
my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)
mutable_seq=my_seq.tomutable()
mutable_seq
mutable-seq[5]="C"
mutable_seq
mutable_seq.remove("T")
mutable_seq
mutable_seq.reverse()
mutable_seq

#Convert back to Seq from mutable_seq
new_seq-mutable_seq.toseq()

#Unknown Seq objects
unk= UnknownSeq(10)
unk
print(unk)
len(unk)
