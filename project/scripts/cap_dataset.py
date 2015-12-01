import pandas as pd

dataset_path = '../data/subreddit_newsubset.csv'
df = pd.read_csv(dataset_path)
subreddit_names = df.subreddit.unique()

limit = 50000

capped_dataset_path = '../data/cappedset_' + str(limit) + '.csv'
subsets = list()

df = pd.read_csv(dataset_path)

for sr in subreddit_names:
    sdf = df[df['subreddit'] == sr]
    sdf = sdf[:limit]
    subsets.append(sdf)

df = pd.concat(subsets)
<<<<<<< d5f73d59042c4156e8db4b0017630a6b59e4bc38
df.to_csv(capped_dataset_path, index=False)
=======
df.to_csv(capped_dataset_path, index = False)
>>>>>>> generate subreddit names from given dataset using pandas
