library('Peptides')
data(AAdata)
files.sources = list.files("~/rpeptides/R")
sapply(files.sources, source)

args<- commandArgs(trailingOnly=TRUE)
option<- args[1]
seq<-args[2]

lag= 1
property= AAdata$Hydrophobicity$KyteDoolittle
property1 = AAdata$Hydrophobicity$KyteDoolittle
property2 = AAdata$Hydrophobicity$Eisenberg

# rpeptide properties:

if(option=="autocovariance"){
  autoCovariance(seq, lag, property)
}
if(option=="aacomp"){
  aaComp(seq)
}
if(option=="aadescriptors"){
  aaDescriptors(seq)
}
if(option== "aindex"){
  aIndex(seq)
}
if(option=="autocorrelation"){
  autoCorrelation(seq, lag, property)
}
if(option=="blosumindices"){
  blosumIndices(seq)
}
if(option=="boman"){
  boman(seq)
  }
if(option=="charge"){
  charge(seq)
  }
if(option=="crosscovariance"){
  crossCovariance(seq, lag, property1, property2)
}
if(option=="crucianiproperties"){
  crucianiProperties(seq)
}
if(option=="fasgaivectors"){
  fasgaiVectors(seq)
}
if(option=="hmoment"){
  hmoment(seq)
}
if(option=="hydrophobicity"){
  hydrophobicity(seq)
}
if(option=="instaindex"){
  instaIndex(seq)
}
if(option=="kiderafactors"){
  kideraFactors(seq)
}
if(option=="lengthpep"){
  lengthpep(seq)
}
if(option=="membpos"){
  membpos(seq)
}
if(option=="mswhimscores"){
  mswhimScores(seq)
}
if(option=="mw"){
  mw(seq)
}
if(option=="pI"){
  pI(seq)
}
if(option=="protFP"){
  protFP(seq)
}
if(option=="stscales"){
  stScales(seq)
}
if(option=="tscales"){
  tScales(seq)
}
if(option=="vhsescales"){
  vhseScales(seq)
}
if(option=="zscales"){
  zScales(seq)
}
