from Bio import SeqIO
from os.path import join

def from_txt():
    files=[]
    while True:
        filetype= input("dataset type: ")
        infile= input("File name with {} data: ".format(filetype))
        if not infile:
            break
        else:
            dir= input("Directory path of file: ")
            # print(directory+infile)
            files.append(join(dir,infile))

        outdir=input("directory of output fasta file: ")
        outfile= input("output fasta file name: ")
        path=join(outdir,outfile)
        file_fasta= open(path, "a+")

        n=0
        t=0

        for file in files:
            # print(file)
            fh=open(file)
            for line in fh:
                # print(line)
                if line.split()[1] not in  SeqIO.to_dict(SeqIO.parse(file_fasta, "fasta"), key_function = lambda rec:rec.seq).keys():
                    file_fasta.write(">{}|{} \n {} \n".format(line.split()[0], filetype, line.split()[1]))
                    n=n+1
            print(n)
            t=t+1        # file_fasta.write(">{} \| %s \n {} \n".format(line.split()[0], filetype, line.split()[1]))
        # print(files[0])
        print(t)



    return path
                    # print("{} \n".format(line.split()))
         # print(files)
    # while input("create more files? ") == "yes":
    #     filetype= input("input the type of dataset file: ")
    #     # if filetype == "positive training":
