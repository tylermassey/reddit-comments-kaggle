import pandas as pd

dataset_path = '../data/subreddit_subset.csv'
subreddit_names = ["gadgets", "sports", "gaming", "news", "history", "music", "funny", "movies", "food", "books"]
limit = 10

capped_dataset_path = '../data/cappedset_' + str(limit) + '.csv'
subsets = list()

df = pd.read_csv(dataset_path)

for sr in subreddit_names:
    sdf = df[df['subreddit'] == sr]
    sdf = sdf[:limit]
    subsets.append(sdf)

df = pd.concat(subsets)
df.to_csv(capped_dataset_path, index = False)