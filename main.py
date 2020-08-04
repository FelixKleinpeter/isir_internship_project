
import pickle
import numpy as np
import pandas as pd

from utils.input_reader import text_input

####

from utils.file_reader import read_lastfm
from recommendation.cleaning import create_experiment_df
from recommendation.recommender import random_forest
from recommendation.functions import get_X, get_y, data_without_v

def user_questions(data, metric, display = False, first_variables = np.array([]), randomness = 0, tags = None):
    new_data = data.copy()
    first_question = False
    if first_variables.size != 0:
        first_question = True

    while new_data.item.unique().size > 10 and len(get_X(new_data).columns) > 1:
        X, y = get_X(new_data), get_y(new_data)
        if first_question:
            v = choose_randomly(X, first_variables, randomness)
            first_question = False
        else:
            v = metric(X, y, randomness = randomness,display=display)

        avg = np.mean(X[v])

        y_or_n = input(str(v)+"? (y/n)")
        # y_or_n = input(question_from_v(v, threshold=avg))
        # y_or_n = input(question_about_music(v, tags))
        if y_or_n == "y" or y_or_n == "Y" or y_or_n == "yes" or y_or_n == "Yes" :
            new_data_ = data_without_v(new_data, v, avg, lower=False)
        elif y_or_n == "n" or y_or_n == "N" or y_or_n == "no" or y_or_n == "No" :
            new_data_ = data_without_v(new_data, v, avg, lower=True)
        if new_data_["item"].size == 0:
            return new_data
        else:
            new_data = new_data_

    return new_data


if __name__ == "__main__":

    #answer = text_input(question)

    LOAD = False

    artists, tags, user_artists, user_friends, user_taggedartists = read_lastfm("recommendation/data/lastfm")

    if not LOAD:
        df = create_experiment_df(user_artists, tags, user_taggedartists, 500)

        filename = 'recommendation/data/experiment_df_lastfm.pkl'
        outfile = open(filename,'wb')
        pickle.dump(df,outfile,protocol=4)
        outfile.close()
    else:
        filename = open('recommendation/data/experiment_df_lastfm.pkl','rb')
        df = pickle.load(filename)
        filename.close()

    print(df.head())

    answers = user_questions(df, random_forest)

    print(answers)
