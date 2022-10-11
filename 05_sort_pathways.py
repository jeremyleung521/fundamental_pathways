import numpy as np
import pickle
from itertools import combinations
import pylcs
import math

with open("04_succ_traj/output.pickle", "rb") as f:
    data = pickle.load(f)
    npathways = len(data)
    lpathways = len(data[0])
    fundamental_pathways = np.zeros((npathways,lpathways,2))
    for idx, val in enumerate(data):
        for idx2, val2 in enumerate(val):
            fundamental_pathways[idx,idx2] = val2

    with open("01_succ_list/output.pickle", "rb") as g:
        data = pickle.load(g)
        npathways = len(data)
        lpathways = len(data[0])
        all_pathways = np.zeros((npathways,lpathways,2))
        results = np.zeros((npathways,7))
        for idx, val in enumerate(data):
            for idx2, val2 in enumerate(val):
                all_pathways[idx,idx2] = val2
    
        for idx, path in enumerate(all_pathways):
#            print(idx, path[0])
    
            results[idx,0] = path[0][0]
            results[idx,1] = path[0][1]

            for fidx, fpath in enumerate(fundamental_pathways):

                pair = np.array([path, fpath])
                seg1 = pair[0][::-1]
                seg2 = pair[1][::-1]
    
                seq1 = pair[0][:,1][::-1]
                seq1_str = ''.join(str(int(x)).zfill(3) for x in seq1)
                seq2 = pair[1][:,1][::-1]
                seq2_str = ''.join(str(int(x)).zfill(3) for x in seq2)
        
                len_seq1 = len(seq1_str)
                len_seq2 = len(seq2_str)
        
                lcsstr = pylcs.lcs_string_length(seq1_str,seq2_str)
                km = int(math.floor(lcsstr)/3)
                similarity = (2*km)/(int(len_seq1/3)+int(len_seq2/3))
            
                results[idx,int(fidx+2)] = similarity

            results[idx,6] = int(np.argmax(results[idx,2:6])+1)
    
    #            with open('./update.txt', 'a') as fo:
    #                fo.write("similarity: "+" "+str(seg1[-1])+" "+str(seg2[-1])+" "+str(km)+" "+str(similarity))
    #                fo.write('\n')
    
    #        print(km, int(len_seq1/3), int(len_seq2/3))
    #        print("segments:",iter1, iter2)
    #        print("similarity =",similarity)
    #        print("--- %s seconds ---" % (time.time() - start_time))

        fmt = '%d', '%d', '%1.3f', '%1.3f', '%1.3f', '%1.3f', '%d'
    
        np.savetxt("05_sorted_pathways.txt", results, fmt=fmt)
