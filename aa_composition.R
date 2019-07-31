Descriptors <- function(seq){
  source('aacomp.R')
  library(Peptides)


  args<-commandArgs(TRUE)
  peptide_sequence = args[1]

  descriptors <- aaComp(seq)
  print(descriptors,row.names=FALSE)
  return (descriptors[1])
}

Descriptors("KWKLFKKIGIGKFLHSAKKF")
