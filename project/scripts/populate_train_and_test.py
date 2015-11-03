import numpy as np
import pandas as pd

reader = pd.read_csv('../data/subreddit_subset.csv',encoding='utf-8', engine="python", chunksize=100000)

np.random.seed(0)

firstChunk = True

for chunk in reader:
	is_test = np.random.uniform(0,1,len(chunk)) > .75

	print "Populating a training chunk"
	train = chunk[is_test == False]
	if firstChunk:
		train.to_csv("train.csv", encoding="utf-8", mode="a", header=True)	
	train.to_csv("../data/train.csv", encoding="utf-8", mode="a", header=None)
	print "train chunk contains", len(train), "rows\n"

	print "Populating a test chunk"
	test = chunk[is_test == True]
	if firstChunk:
		test.to_csv("../data/test.csv", encoding="utf-8", mode="a", header=True)
		firstChunk = False	
	test.to_csv("../data/test.csv", encoding="utf-8", mode="a", header=None)
	print "test chunk contains", len(test), "rows\n"



trainSet = pd.read_csv("../data/train.csv",encoding="utf-8")
print "Populating a toy set"
toy = trainSet.sample(n=2000, random_state=0)
toy.to_csv("../data/toy.csv", encoding='utf-8')