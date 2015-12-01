import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

limit = 50000

dataset_path = '../data/cappedset_' + str(limit) + '.csv'
train_set_path = '../data/train_set_cap' + str(limit) + '.csv'
test_set_path = '../data/test_set_cap' + str(limit) + '.csv'
toy_train_set_path = '../data/toy_train_set_cap' + str(limit) + '.csv'
toy_test_set_path = '../data/toy_test_set_cap' + str(limit) + '.csv'

df = pd.read_csv(dataset_path)
r_train = np.random.RandomState(20)
r_test = np.random.RandomState(30)
r = np.random.RandomState(43)

train_set, test_set = train_test_split(df, train_size=0.8, random_state=r)
# toy_train_set = train_set.sample(2000, random_state=r_train)
# toy_test_set = train_set.sample(2000, random_state=r_test)

train_set.to_csv(train_set_path, index=False)
test_set.to_csv(test_set_path, index=False)
# toy_train_set.to_csv(toy_train_set_path, index=False)
# toy_test_set.to_csv(toy_test_set_path, index=False)
