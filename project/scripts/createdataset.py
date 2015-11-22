import numpy as np
import pandas as pd
import sqlite3
import re
import HTMLParser
from nltk.corpus import stopwords

NO_APPOSTROPHE = { "youre" : "you are", "theyre" : "they are", "im" : "i am",
        "hes" : "he is", "shes" : "she is", "its" : "it is", "aint" : "am not",
        "arent" : "are not", "couldnt" : "could not", "doesnt" : "does not",
        "hasnt" : "has not", "hadnt" : "had not" }

APPOSTROPHE = { "s" : "is", "'re" : "are", "m" : "am", "ll" : "will",
        "d" : "had", "ve" : "have"}

subreddit_dict = {}
i = 0 

def get_index(row) :
    if row['subreddit'] in subreddit_dict :
        return subreddit_dict[row['subreddit']]
    else :
        subreddit_dict[row['subreddit']] = i 
        global i
        i += 1
        return subreddit_dict[row['subreddit']]


def comment_under_post(row):
    return row["parent_id"].startswith("t1")

def replace_two_or_more(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def clean_string(s) :
    if  s == "[deleted]":        
        s = np.nan
        return s

    # convert those &amp -> '&', &lt -> '<'... etc
    s = html_parser.unescape(s)
    # www.* AND https:* -> '
    s = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', s)

    s = s.lower()

    # ex. Helloooooooooo -> helloo
    s = replace_two_or_more(s)

    # list words with alphabets, numbers, and underscores
    s = re.split(r'\W+', s)

    for i, word in enumerate(s) :

        if word in NO_APPOSTROPHE:
            split_words = NO_APPOSTROPHE[word].split()
            s[i] = split_words[0]
            s.append(split_words[1])

        if word in APPOSTROPHE:
            s[i] = APPOSTROPHE[word]

    # removing stopwords from NLTK
    s  = [word for word in s if word not in stopwords.words('english')]
    # remove any empty element
    s = filter(None, s)
    # concatnate to a string
    s  = ' '.join(s)
    s.decode("utf8").encode('ascii', 'ignore')
    if s == '':
        s = np.nan
    return s

# Make sure to change this sqlite db path
db_filepath = "/Users/lee/practice/big_data/data/database.sqlite"
csv_filepath = "/Users/lee/practice/big_data/data/subreddit_subset.csv"

db_con = sqlite3.connect(db_filepath)

reader = pd.read_sql("select * from May2015", con=db_con, chunksize=100000)

firstChunk = True
html_parser = HTMLParser.HTMLParser()


for chunk in reader:
    chunk = chunk[['body', 'parent_id', 'subreddit']]
    
    chunk['body'] = chunk['body'].apply(clean_string)
    chunk.dropna(inplace=True) 
    chunk['subreddit_index']= chunk.apply(lambda row: get_index(row), axis = 1) 
    chunk['comment_under_post'] = chunk.apply(lambda row: comment_under_post(row), axis=1)

    chunk = chunk[chunk['subreddit'].isin(
        ['gadgets', 'sports', 'gaming', 'news', 'history', 'music', 'funny', 'movies', 'food', 'books'])]

    if firstChunk:
        chunk.to_csv(path_or_buf=csv_filepath, sep=',', mode='a', index=False,
                     header=['body', 'parent_id', 'subreddit', 'comment_under_post', 'subreddit_index'])
        firstChunk = Fae

    # print chunk
    chunk.to_csv(path_or_buf=csv_filepath, sep=',', mode='a', index=False, header=None)
