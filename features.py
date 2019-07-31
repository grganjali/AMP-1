import re
from codes import *

args={}

args['file']= "{}".format(input("input filename: "))
args['type']= "{}".format(input("input typename: "))

# print(args)
fastas = readFasta.readFasta(args.file)
userDefinedOrder = args.userDefinedOrder if args.userDefinedOrder != None else 'ACDEFGHIKLMNPQRSTVWY'
userDefinedOrder = re.sub('[^ACDEFGHIKLMNPQRSTVWY]', '', userDefinedOrder)
if len(userDefinedOrder) != 20:
    userDefinedOrder = 'ACDEFGHIKLMNPQRSTVWY'
myAAorder = {
    'alphabetically': 'ACDEFGHIKLMNPQRSTVWY',
    'polarity': 'DENKRQHSGTAPYVMCWIFL',
    'sideChainVolume': 'GASDPCTNEVHQILMKRFYW',
    'userDefined': userDefinedOrder
}
myOrder = myAAorder[args.order] if args.order != None else 'ACDEFGHIKLMNPQRSTVWY'
kw = {'path': args.filePath, 'train': args.trainFile, 'label': args.labelFile, 'order': myOrder}

myFun = args.type + '.' + args.type + '(fastas, **kw)'
print('Descriptor type: ' + args.type)
encodings = eval(myFun)
outFile = args.outFile if args.outFile != None else 'encoding.tsv'
saveCode.savetsv(encodings, outFile)
