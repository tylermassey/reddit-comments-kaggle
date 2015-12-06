import sys
import numpy as np
import pandas as pd

dataset_path = '../data/subreddit_newsubset.csv'
df = pd.read_csv(dataset_path)
subreddit_names = df.subreddit.unique()
cap_size = int(sys.argv[1])
num_outputs = int(sys.argv[2])
r = np.random.RandomState(1234)
output_file_part = '../data/cappedset_' + str(cap_size)

df = pd.read_csv(dataset_path)

for i in range(num_outputs):
    subsets = list()
    for sr in subreddit_names:
        sdf = df[df['subreddit'] == sr]
        sdf = sdf.sample(n=cap_size, random_state=r)
        subsets.append(sdf)
    capped_dataset_path = output_file_part + '_' + str(i) + '.csv'
    df_2 = pd.concat(subsets)
    df_2.to_csv(capped_dataset_path, index=False)
