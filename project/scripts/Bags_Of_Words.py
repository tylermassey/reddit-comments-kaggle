import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
   
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
