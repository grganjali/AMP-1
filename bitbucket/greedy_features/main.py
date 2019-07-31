import os
import pandas as pd
import pickle
import time


PROJECT_DIR = "/home/chmrodrigues/Documents/greedy_features"
DATA_DIR = "/home/chmrodrigues/Documents/greedy_features/data"
OUTPUT_DIR = "/home/chmrodrigues/Documents/greedy_features/results"
AUTOSKLEARN_DIR = "/home/chmrodrigues/Documents/autosklearn"

# CAPRI DATASETS TO BLINDTEST
CAPRI1 = os.path.join(DATA_DIR,"T55_all.csv")
CAPRI2 = os.path.join(DATA_DIR,"T56_all.csv")

def main():
    # READ DATASET FILE WITH ALL FEATURES
    dataset_training = os.path.join(DATA_DIR, "foldx_centrality_metrics_index3_rpeptides_residue_environment_index21_substables_diff_contacts_bio3d_ifeature.csv")
    df_training = pd.read_csv(dataset_training)
    # READ CSV WITH RANK OF FEATURES
    features_rank = os.path.join(DATA_DIR, "features_rank.csv")
    df_attrs_rank = pd.read_csv(features_rank)

    # FIX BEST ATTR ACCORDING TO RANK
    attr_combination = ['rsa']
    # READ ALL OTHER ATTRIBUTES EXCEPT THE BEST ONE
    bag_attrs = df_attrs_rank['attr']
    bag_attrs = [item for item in bag_attrs if item != "rsa"]

    # OUTPUT RESULTS LIST
    output_results = list()

    # UNTIL ALL THE ATTRIBUTES ARE PART OF A COMBINATION
    while len(bag_attrs) != 0:
        best_attr = None
        best_score = 0.0
        # COMBINE THE FIXED LIST WITH EVERY ATTRIBUTE REMAINING
        for attr in bag_attrs:
            identifier = str(time.time()).replace('.','')

            attrs2test = attr_combination + [attr,'ddg'] 
            df2test = df_training[attrs2test]
            df2test.to_csv("{}/training_{}.csv".format(DATA_DIR, identifier),index=False)
            # TRAIN AND TEST
            os.system("python {}/train_test_capri.py -t {}/training_{}.csv -c ddg -b1 {} -b2 {} -o {}".format(AUTOSKLEARN_DIR, DATA_DIR, identifier, CAPRI1, CAPRI2, OUTPUT_DIR))
            # PARSE RESULTS
            results_lines = [item.strip() for item in open("{}/training_{}.csv.performance_test_all.csv".format(OUTPUT_DIR,identifier),"r").readlines()]

            # CHECK IF ANY OF THE RESULTS ARE GREATER THAN THE BEST COMBINATION
            for result in results_lines[1:]:
                score = float(result.split()[1])
                if score > best_score:
                    best_score = score
                    best_attr = attr
        # STORE BEST COMBINATION OF LENGTH i
        attr_combination.append(best_attr)
        # REMOVE BEST ATTRIBUTE FOR LENGTH i
        bag_attrs.remove(best_attr)
        # STORE BEST RESULT ON RESULTS LIST
        output_results.append((len(attr_combination),best_score,attr_combination))

    # WRITE RESULTS LIST TO PICKLE FILE
    pickle.dump(output_results, open('{}/grid_features.p'.format(OUTPUT_DIR),'wb'),protocol=2)

    return True


if __name__ == "__main__":
    main()
