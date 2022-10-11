import numpy as np

data = np.loadtxt("02_similarities.txt").astype(np.float64)

for pair in data:
    if pair[4] > 0.5:
        print(str(int(pair[2])).zfill(3)+str(int(pair[3])).zfill(3))

