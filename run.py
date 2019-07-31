from os.path import isfile,join
from os import listdir

indir=input("directory name containing R files: ")
files = [join(indir,f) for f in listdir(indir) if isfile(join(indir, f))]
import pdb; pdb.set_trace()
for file in files:
    ftemp= open("temp.txt", 'a+')
    ftemp.write("source('aaCheck.R')")
    f=open(file)
    content= f.read()
    ftemp.writelines(content)
    ftemp.close()
    ftemp= open("temp.txt", 'w+')
    final=ftemp.read()
    f.writelines(final)
    f.close()
