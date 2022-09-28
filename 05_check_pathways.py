import numpy as np
import pickle
from itertools import combinations

with open("04_succ_traj/output.pickle", "rb") as f:
    data = pickle.load(f)
    npathways = len(data)
    lpathways = len(data[0])
    pathways = np.zeros((npathways,lpathways,2))
    for idx, val in enumerate(data):
        for idx2, val2 in enumerate(val):
            pathways[idx,idx2] = val2

    print(pathways[:,0])
