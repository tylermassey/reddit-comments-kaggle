import numpy as np
import pandas as pd

print "Reading the subset.csv file"
df = pd.read_csv('/Users/lee/practice/big_data/reddit-comments-kaggle/project/data/subreddit_subset.csv',encoding='utf-8', engine='python')
print "Subset contains ", len(df), " rows"

np.random.seed(0)
is_test = np.random.uniform(0, 1, len(df)) > .75

print "Populating a training set"
train = df[is_test == False]
train.to_csv("train.csv", sep="\t", encoding='utf-8')
print "train contains", len(train), "rows\n"

print "Populating a test set"
test = df[is_test == True]
test.to_csv("test.csv", sep="\t", encoding='utf-8')
print "train contains", len(test), "rows\n"

print "Populating a toy set"
toy = train.sample(n=2000, random_state=0)
toy.to_csv("toy.csv", sep="\t", encoding='utf-8')
