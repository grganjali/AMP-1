import subprocess
from sys import argv
from os.path import join
from subprocess import Popen, PIPE
# indir= input("routputs directory: ")
# files = [join(indir,f) for f in listdir(indir) if isfile(join(indir, f))]

# file= open("routputs/s1.txt", "a+")

option= input("Which property to calculate: ")
seq= input("enter sequence: ")

def composition(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)
    # print(output)
    # import pdb; pdb.set_trace()
    output = output.decode().split("\n")

    output_dict = dict()
    for i in range(2,11):
        values = output[i].split()
        output_dict[values[0]] = dict()
        output_dict[values[0]]['number'] = "{}".format(values[1])
        output_dict[values[0]]['percentage'] = "{}".format(values[2])

    print(output_dict)
    # file.write(str(output_dict))

# ' @title Compute 66 descriptors for each amino acid of a protein sequence.
def descriptors(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)
    print(output)
    return output

#' @title Compute the aliphatic index of a protein sequence
def aindex(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)
    print(output)

#' @title Compute the auto-correlation index of a protein sequence
def autocorrelation(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the auto-covariance index of a protein sequence
def autocovariance(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the BLOSUM62 derived indices of a protein sequence
def blosumIndices(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)
    print(output)
    return output


#' @title Compute the Boman (Potential Protein Interaction) index
def boman(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the theoretical net charge of a protein sequence
def charge(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the cross-covariance index of a protein sequence
def crosscovariance(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)
    print(output)

#' @title Compute the Cruciani properties of a protein sequence
def crucianiProperties(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the FASGAI vectors of a protein sequence
def fasgaiVectors(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the hydrophobic moment of a protein sequence
def hmoment(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the hydrophobicity index of a protein sequence
def hydrophobicity(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the instability index of a protein sequence
def instaindex(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the Kidera factors of a protein sequence
def kinderaFactors(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the amino acid length of a protein sequence
def lengthpep(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute theoretically the class of a protein sequence
def membpos(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the MS-WHIM scores of a protein sequence
def mswhimScores(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the molecular weight of a protein sequence
def mw(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the isoelectic point (pI) of a protein sequence
def pI(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the protFP descriptors of a protein sequence
def protFP(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the ST-scales of a protein sequence
def stScales(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)



#' @title Compute the T-scales of a protein sequence
def tScales(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the VHSE-scales of a protein sequence
def vhseScales(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


#' @title Compute the Z-scales of a protein sequence
def zScales(option, seq):
    output = subprocess.check_output(["Rscript test3.R {} {}".format(option, seq) ], shell=True)


crosscovariance(option, seq)
