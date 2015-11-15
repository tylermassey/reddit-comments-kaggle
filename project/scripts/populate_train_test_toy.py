import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

dataset_path = '../data/subreddit_subset.csv'
train_set_path = '../data/train_set.csv'
test_set_path = '../data/test_set.csv'
toy_set_path = '../data/toy_set.csv'

df = pd.read_csv(dataset_path)
r = np.random.RandomState(43)

train_set, test_set = train_test_split(df, train_size=0.8, random_state=r)
toy_set = train_set.sample(2000, random_state=r)

train_set.to_csv(train_set_path, index=False)
test_set.to_csv(test_set_path, index=False)
toy_set.to_csv(toy_set_path, index=False)