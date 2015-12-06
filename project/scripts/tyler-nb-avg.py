import sys
import numpy as np
import pandas as pd
import gc
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

names = ['nba', 'relationships', 'todayilearned', 'leagueoflegends', 'AdviceAnimals', 'news', 'movies', 'nfl',
         'CasualConversation', 'hockey']
labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cap_size = int(sys.argv[1])
num_files = int(sys.argv[2])
output_file_part = '../data/cappedset_' + str(cap_size) + '_'

results = list()

for i in range(num_files):
    capped_file = output_file_part + str(i) + '.csv'
    r = np.random.RandomState(43)

    df = pd.read_csv(capped_file)
    train_df, test_df = train_test_split(df, train_size=0.90, random_state=r)
    del df
    gc.collect()

    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer(norm='l2', sublinear_tf=True)),
                         ('clf', MultinomialNB())])
    text_clf = text_clf.fit(train_df.body, train_df.subreddit_index)
    predicted = text_clf.predict(test_df.body)
    results.append(np.mean(predicted == test_df.subreddit_index))
    print "capped file " + str(i) + " : " + str(results[i])

average = np.average(results)
print "average = " + str(average)
