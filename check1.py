import pickle
import sys

# list=[1,2,3]
# file= "file_pickle"
# fh= open(file, "wb")
# pickle.dump(list, fh)
#
# print("OUTPUT")
# fh.close()
# fh=open(file, "rb")
# outlist= pickle.load(fh)
# print(outlist)
#
# print(list==outlist)



arglist= ["iFeature.py", "--file examples/test-peptide.txt", "--type EAAC"]
sys.argv= arglist
print(sys.argv)
