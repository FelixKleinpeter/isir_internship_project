

import numpy as np
import pandas as pd

def data_without_v(data, variable, value, lower=True):
    d = data.copy()
    if lower:
        d = d[d[variable] < value]
    else:
        d = d[d[variable] > value]
    d.drop([variable], axis=1, inplace=True)
    return d

def get_X(data):
    X = data.copy()
    X.drop(['rating','item','user'], axis=1, inplace=True)
    return X

def get_y(data):
    y_ = data.rating.copy()
    y__ = [round(e) for e in y_]
    y = [0 if e < 4 else 1 for e in y__]
    return y
