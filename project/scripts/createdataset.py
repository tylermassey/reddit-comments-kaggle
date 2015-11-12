import numpy as np
import pandas as pd
import sqlite3

# Make sure to change this sqlite db path
db_filepath = "/Users/tylermassey/Desktop/database.sqlite"
csv_filepath = "../data/subreddit_subset.csv"

db_con = sqlite3.connect(db_filepath)
reader = pd.read_sql("select * from May2015", con=db_con, chunksize=100000)


def comment_under_post(row):
    return row["parent_id"].startswith("t1")


firstChunk = True
for chunk in reader:
    chunk = chunk[['body', 'parent_id', 'subreddit']]

    # this whole section needs to be optimized
    chunk.replace('', np.nan, inplace=True)
    chunk.dropna(inplace=True)
    chunk['comment_under_post'] = chunk.apply(lambda row: comment_under_post(row), axis=1)
    chunk['body'] = chunk['body'].str.replace('[^\w\s]', ' ')
    chunk['body'] = chunk['body'].str.replace('\n', ' ')
    chunk['body'] = chunk['body'].str.replace('\t', ' ')
    chunk['body'] = chunk['body'].str.replace('\r', ' ')

    chunk = chunk[chunk['subreddit'].isin(
        ['gadgets', 'sports', 'gaming', 'news', 'history', 'music', 'funny', 'movies', 'food', 'books'])]

    if firstChunk:
        chunk.to_csv(path_or_buf=csv_filepath, sep=',', mode='a', index=False,
                     header=['body', 'parent_id', 'subreddit', 'comment_under_post'])
        firstChunk = False
        print "chunk saved"

    chunk.to_csv(path_or_buf=csv_filepath, sep=',', mode='a', index=False, header=None)
    print "chunk saved"
