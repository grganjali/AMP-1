#starting
import rpy2
print(rpy2.__version__)

#r objects
import rpy2.robjects as robjects

#importing r packages
from rpy2.robjects.packages import importr
base= import('base')#creates python object base
utils= importr('utils')#creates python object base

#installing r packages
import rpy2.robjects.packages as rpackages
utils=rpackages.importr('utils')
#selecting the first mirror in the mirror known to R
utils.chooseCRANmirror(ind=1)

#install r packages:
packnames= ['ggplot2', 'hexbin']
#r vector of strings
from rpy2.robjects.vectors import StrVector
names_to_install= [x for packnames if not rpackages.isinstalled(x)]
if len(names_to_install)>0:
    utils.install_packages(StrVectors(names_to_install))

#the r instance: rpy2.robjects.r

#getting r objects
pi= robjects.r('pi')
pi

#r code example:
robjects.r('''
        # create a function `f`
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        # call the function `f` with argument value 3
        f(3)
        ''')

r_f= robjects.glovalenv('f')
#or
R_f= robjects.r('f')
print(r_f, verbose = FALSE)
r_f(3)
