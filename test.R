library("Peptides")
# source('rpeptides/R/autocorrelation.R')
data(AAdata)


args <- commandArgs(trailingOnly= TRUE)
seq <-args[1]
lag=1
property=AAdata$Hydrophobicity$KyteDoolittle

# print(property)

# Calculate the auto-correlation index for a lag=1
autoCorrelation(seq, lag,  property, center = TRUE)


#'Calculate the auto-covariance index for a lag=1
 autoCovariance(seq, lag, property, center= TRUE)

# aaDescriptors(seq)

blosumIndices(seq)
