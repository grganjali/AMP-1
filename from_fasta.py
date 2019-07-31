from Bio import SeqIO
from os.path import join
# import time


# start_time= time.time()

def from_fasta():

    files=[]
    while True:
        infile= input("File name: ")
        if not infile:
            break
        else:
            dir= input("Directory path of file: ")
            # print(directory+infile)
            files.append(join(dir,infile))

    # while True:
    #     filename= str(input("File name: "))
    #     if not filename:
    #         break
    #     files.append(filename)

    outdir=input("directory of output fasta file: ")
    outfile= input("output fasta file name: ")
    path=join(outdir,outfile)
    file_fasta= open(path, "a+")

    n=0
    t=0
    for file in files:
        for seq_record in SeqIO.parse(file, "fasta"):
            if ("Predicted" not in seq_record.description.split('|')) and (seq_record.seq not in  SeqIO.to_dict(SeqIO.parse(file_fasta, "fasta"), key_function = lambda rec:rec.seq).keys()):
                n=n+SeqIO.write(seq_record, file_fasta, "fasta") # returns the no. of records added in one iteration
        print(n) #Total no. of recors in final fasta
        t=t+1
    print(t)
    return path

# print("------------%s seconds------------ "%(time.time()-start_time))
# print(SeqIO.to_dict(SeqIO.parse(files[0], "fasta")).keys())
# print(SeqIO.to_dict(SeqIO.parse(files[0], "fasta"), key_function = lambda rec:rec.seq).keys())
