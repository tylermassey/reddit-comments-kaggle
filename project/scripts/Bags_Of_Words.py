import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def subreddit_index(row):
    #This function need to be applied to dataframe
    #Assigns each subreddit a unique integer

    if row["subreddit"] == "gadgets":
        return 1;
    elif row["subreddit"] == "sports":
        return 2;
    elif row["subreddit"] == "gaming":
        return 3;
    elif row["subreddit"] == "news":
        return 4;
    elif row["subreddit"] == "history":
        return 5;
    elif row["subreddit"] == "music":
        return 6;
    elif row["subreddit"] == "funny":
        return 7;
    elif row["subreddit"] == "movies":
        return 8;
    elif row["subreddit"] == "food":
        return 9;
    else:
        return 10;
    
def Bags_Of_Words(train_fp, test_fp, freq_flag):
    #This function will a dictionary of bags of words
        #one will be the training bag of words and one will be the test bag of words
    
    #train_fp is the filepath to the dataset
    #test_fp is a CountVectorizer object you need to pass in
    #freq_flag will determine if you want to consider either occurence or frequency when making bags of words
        #Could affect how accurate our model is 
    
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    
    df_train = pd.read_csv(train_fp)
    df_test = pd.read_csv(test_fp)

    #Adds a new column called subreddit_index to dataframe using subreddit_index function
    df_train["subreddit_index"] = df_train.apply(lambda row: subreddit_index(row), axis=1)
    df_test["subreddit_index"] = df_test.apply(lambda row: subreddit_index(row), axis=1)

    #Only keep parent comments
    # df = df[df.comment_under_post != False]

    X_train_counts = count_vect.fit_transform(df_train.body)
    X_test_counts = count_vect.transform(df_test.body)

    #Takes into account comment length, transforms matrix into frequency of a particular word, not simply occurence
    if(freq_flag):
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)
        return {'train':X_train_tfidf, 'test':X_test_tfidf}
    else:
        return {'train':X_train_counts, 'test':X_test_counts}