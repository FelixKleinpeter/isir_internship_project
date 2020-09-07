#coding:utf-8


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from recommendation.functions import get_X, get_y, data_without_v


def choose_randomly(data, variables, randomness):
    fe = variables.copy()
    if np.max(fe) == 0:
        return data.columns[np.random.choice(len(fe))]
    fe = [i / np.max(fe) for i in fe]
    fe = [i  if i >= (1-randomness) else 0 for i in fe]
    fe = [i / sum(fe) for i in fe]
    v_i = np.random.choice(len(fe), p=fe)
    return data.columns[v_i]

# Random Forest selection
def random_forest(X, y, display=False, max_depth=7, randomness = 0):
    clf = RandomForestClassifier(max_depth=max_depth, random_state=0)
    clf.fit(X, y)
    fe = clf.feature_importances_
    v = choose_randomly(X, fe, randomness)
    return v, fe
