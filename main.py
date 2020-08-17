
import numpy as np
import pandas as pd
import time

from utils.input_reader import text_input
from utils.file_reader import experiment_lastfm
from utils.generator.question import question_from_v_musics
from utils.generator.xml_file import xml_from_question
from utils.output_displayer import lastfm_output_displayer
from utils.network.file_sender import send_to_greta
from utils.functions import clean_directory

from precomputation.lastfm import first_variable_precomputation
from behaviour.behaviour import behaviour_lastfm

####

from utils.file_reader import read_lastfm
from recommendation.recommender import random_forest, choose_randomly
from recommendation.functions import get_X, get_y, data_without_v







if __name__ == "__main__":

    # Loading or computing the process dataframe
    LOAD = False
    df, tags, artists = experiment_lastfm("recommendation/data",load=LOAD)

    # Parameters
    randomness = 0.7
    input_function = text_input
    question_function = question_from_v_musics
    behaviour = "COMP" # "WARM" or "COMP"
    networking = False

    # Loading or computing the first variables / variables tree
    first_variables = first_variable_precomputation(df, randomness)

    # Creating question depending on the selected behaviour
    questions = behaviour_lastfm(behaviour)

    # Question counter
    question_amount = 0

    experiment_data = df.copy()
    while experiment_data.item.unique().size > 10 and len(get_X(experiment_data).columns) > 1:
        X, y = get_X(experiment_data), get_y(experiment_data)
        if question_amount == 0:
            v = choose_randomly(X, first_variables, randomness)
        else:
            v, _ = random_forest(X, y, randomness = randomness)
        avg = np.mean(X[v])
        question = question_function(v, tags, questions)
        if len(questions) > 0:
            del questions[0]

        filename = "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml"
        xml_from_question(question, filename)
        if networking:
            send_to_greta("output/" + filename)

        y_or_n = input_function(question)

        if y_or_n == "y" or y_or_n == "Y" or y_or_n == "yes" or y_or_n == "Yes" :
            experiment_data_ = data_without_v(experiment_data, v, avg, lower=False)
        elif y_or_n == "n" or y_or_n == "N" or y_or_n == "no" or y_or_n == "No" :
            experiment_data_ = data_without_v(experiment_data, v, avg, lower=True)
        if experiment_data_["item"].size == 0:
             user_preferences = experiment_data
             break
        else:
            experiment_data = experiment_data_
            user_preferences = experiment_data
        question_amount += 1

    recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
    print(recommendations)
    #print("Question amount %s " % question_amount)

    clean_directory('output')
