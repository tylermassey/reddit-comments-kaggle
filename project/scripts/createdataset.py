import numpy as np
import pandas as pd
import sqlite3

# Make sure to change this sqlite db path
db_filepath = "/Users/tylermassey/Desktop/database.sqlite"
csv_filepath = "../data/subreddit_subset.csv"

db_con = sqlite3.connect(db_filepath)
reader = pd.read_sql("select * from May2015", con=db_con, chunksize=100000)

firstChunk = True

for chunk in reader:
	gadgets 	= chunk['subreddit'] == "gadgets"
	sports		= chunk['subreddit'] == "sports"
	gaming		= chunk['subreddit'] == "gaming"
	news		= chunk['subreddit'] == "news"
	history		= chunk['subreddit'] == "history"
	music		= chunk['subreddit'] == "music"
	funny		= chunk['subreddit'] == "funny"
	movies		= chunk['subreddit'] == "movies"
	food		= chunk['subreddit'] == "food"
	books		= chunk['subreddit'] == "books"
	
	chunk = chunk[gadgets | sports | gaming |
			news | history | music | funny | 
			movies | food | books]

	if firstChunk:
		chunk.to_csv(path_or_buf=csv_filepath,mode="a",encoding='utf-8',header=True)
		firstChunk = False;

	chunk.to_csv(path_or_buf=csv_filepath,mode="a",encoding='utf-8',header=None)