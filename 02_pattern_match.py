import numpy as np
import pickle
from itertools import combinations
import time
import pylcs
import math

with open("../output.pickle", "rb") as f:
    data = pickle.load(f)
    npathways = len(data)
    lpathways = len(data[0])
    pathways = np.zeros((npathways,lpathways,2))
    for idx, val in enumerate(data):
        for idx2, val2 in enumerate(val):
            pathways[idx,idx2] = val2

    #print(pathways.shape)

    perm = combinations(pathways,2)
    a = np.array(list(perm), dtype=np.int64)

    similarities = np.zeros((a.shape[0],5))

    for idx, pair in enumerate(a):

        seg1 = pair[0][::-1]
        seg2 = pair[1][::-1]

        seq1 = pair[0][:,1][::-1]
        seq1_str = ''.join(str(int(x)).zfill(3) for x in seq1)
        seq2 = pair[1][:,1][::-1]
        seq2_str = ''.join(str(int(x)).zfill(3) for x in seq2)
    
        len_seq1 = len(seq1_str)
        len_seq2 = len(seq2_str)
    
        start_time = time.time()
        lcsstr = pylcs.lcs_string_length(seq1_str,seq2_str)
        km = int(math.floor(lcsstr)/3)
        similarity = (2*km)/(int(len_seq1/3)+int(len_seq2/3))
        
        similarities[idx,0] = seg1[-1][0]
        similarities[idx,1] = seg1[-1][1]
        similarities[idx,2] = seg2[-1][0]
        similarities[idx,3] = seg2[-1][1]
        similarities[idx,4] = similarity

        with open('./update.txt', 'a') as fo:
            fo.write("similarity: "+" "+str(seg1[-1])+" "+str(seg2[-1])+" "+str(km)+" "+str(similarity))
            fo.write('\n')

#        print(km, int(len_seq1/3), int(len_seq2/3))
#        print("segments:",iter1, iter2)
#        print("similarity =",similarity)
#        print("--- %s seconds ---" % (time.time() - start_time))

    np.savetxt("output/02_similarities.txt", similarities)
