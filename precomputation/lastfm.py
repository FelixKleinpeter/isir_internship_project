
import pickle
from os import path

from recommendation.functions import get_X, get_y
from recommendation.recommender import random_forest

def first_variable_precomputation(df,randomness):
    filename = "precomputation/data/lastfm_first_variable.pkl"

    if path.exists(filename):
        f = open(filename,'rb')
        first_variables = pickle.load(f)
        f.close()
    else:
        X, y = get_X(df), get_y(df)
        _, first_variables = random_forest(X, y, randomness = randomness)
        f = open(filename,'wb')
        pickle.dump(first_variables,f,protocol=4)
        f.close()

    return first_variables
