import subprocess
import pandas as pd
import sys
import pickle

def deploy(seq):

    features=   ["aacomp",
                "aindex",
                'autocovariance',
                'autocorrelation',
                'blosumindices',
                'boman',
                'charge',
                'crosscovariance',
                'crucianiproperties',
                'fasgaivectors',
                'hmoment',
                'hydrophobicity',
                'instaindex',
                'kiderafactors',
                'lengthpep',
                'mswhimscores',
                'mw',
                'pI',
                'protFP',
                'stscales',
                'tscales',
                'vhsescales',
                'zscales']
    # df= pd.read_csv("datasets/sequence.csv")
    # sequences= df.sequence
    # print(len(sequences))
    # print(sequences)
    # seq= sys.argv[1]
    # num= sys.argv[2]
    # start_time= datetime.now()
    seq_dict=dict()

    seq_name= dict()
    seq_name["seq"]= "{}".format(seq)

    seq_dict.update(seq_name)

    # option= input("Which property to calculate: ")
    # seq= input("enter sequence: ")

    # for seq in sequences:
    # print(seq)

    for option in features:
        # print(option)

        def getout(option, seq):
            try:
                output= subprocess.check_output(["Rscript /home/local/BHRI/agarg/06/test3.R {} {}".format(option, seq) ], shell=True)
            except subprocess.CalledProcessError as e:
                raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
            return(output)

        output=getout(option, seq)
        # print(output)

        if( option== "aacomp"):
            output = output.decode().split("\n")

            output_dict = dict()
            # import pdb; pdb.set_trace()
            for i in range(3,12):
                values = output[i].split()
                output_dict[values[0]] = dict()
                output_dict[values[0]]['number'] = "{}".format(values[1])
                output_dict[values[0]]['percentage'] = "{}".format(values[2])

            seq_dict.update(output_dict)

        if(option=="aadescriptors"):
            output= output.decode().split("\n")
            output_dict= dict()
            keys= list()
            values= list()
            for i in range(1, 513, 2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values[1:])

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)


        if(option=="aindex"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)


        if(option=="autocorrelation"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="autocovariance"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="blosumindices"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            for i in range(2,6,2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values)
            # print(keys, values)

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]

            seq_dict.update(output_dict)


        if(option=="boman"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="charge"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)




        if(option=="crosscovariance"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)




        if(option=="crucianiproperties"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            keys= output[2].split()
            values= output[3].split()
            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)


        if(option=="fasgaivectors"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            keys= output[2].split()
            values= output[3].split()
            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)



        if(option=="hmoment"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="hydrophobicity"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict);




        if(option=="instaindex"):

            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="kiderafactors"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            for i in range(2,6,2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values)

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]

            seq_dict.update(output_dict)


        if(option=="lengthpep"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)




        if(option=="membpos"):
            output = output.decode().split("\n")
            output = [item for item in output if len(item) > 0]

            output_dict = dict()
            for i in range(3,len(output[3:])):
                values = output[i].split()
                output_dict[values[1]] = dict()
                output_dict[values[1]]['H'] = "{}".format(values[2])
                output_dict[values[1]]['uH'] = "{}".format(values[3])
                output_dict[values[1]]['MembPos'] = "{}".format(values[4])

            seq_dict.update(output_dict)



        if(option=="mswhimscores"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            keys= output[2].split()
            values= output[3].split()
            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)



        if(option=="mw"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)



        if(option=="pI"):
            output= output.decode().split("\n")
            output_dict={"{}".format(option): "{}".format(output[1].split()[1])}
            seq_dict.update(output_dict)




        if(option=="protFP"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            for i in range(2,6,2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values)

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]

            seq_dict.update(output_dict)



        if(option=="stscales"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            for i in range(2,6,2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values)

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]

            seq_dict.update(output_dict)


        if(option=="tscales"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            keys= output[2].split()
            values= output[3].split()
            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)




        if(option=="vhsescales"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            for i in range(2,6,2):
                key_values= output[i].split()
                keys.extend(key_values)
                val_values= output[i+1].split()
                values.extend(val_values)

            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]

            seq_dict.update(output_dict)



        if(option=="zscales"):
            output=output.decode().split("\n")
            keys= list()
            values= list()
            output_dict= dict()
            keys= output[2].split()
            values= output[3].split()
            for i in range(0, len(keys)):
                output_dict[keys[i]]= values[i]
            seq_dict.update(output_dict)

    return pd.DataFrame.from_dict(seq_dict)
    # pfile= open("/data/outputs_cdhit/out{}.txt".format(num), "wb+")
    # pickle.dump(seq_dict, pfile)
    # pfile.close()
    # print(seq_dict)

# seq= input("sequence: ")
# out= deploy(seq)
# print(out)
