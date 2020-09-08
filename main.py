
import numpy as np
import pandas as pd
import time
from tkinter import *
import tkinter.font as tkFont

from utils.input_reader import text_input, audio_input, yes_answers, no_answers, idk_answers
from utils.file_reader import experiment_lastfm
from utils.generator.question import question_from_v_musics
from utils.output_displayer import lastfm_output_displayer
from utils.functions import clean_directory, display

from precomputation.lastfm import first_variable_precomputation
from behaviour.behaviour import behaviour_lastfm, introduction_lastfm

####

from utils.file_reader import read_lastfm
from recommendation.recommender import random_forest, choose_randomly
from recommendation.functions import get_X, get_y, data_without_v




if __name__ == "__main__":

    # Loading or computing the process dataframe
    FORCE_CREATE = False
    df, tags, artists = experiment_lastfm("recommendation/data",force_create=FORCE_CREATE)

    # Parameters
    randomness = 0.7
    input_function = text_input
    question_function = question_from_v_musics
    behaviour = "WARM" # "WARM" or "COMP"
    networking = False

    # Loading or computing the first variables / variables tree
    first_variables = first_variable_precomputation(df, randomness)

    # Question counter
    question_amount = 0

    # Output matchers
    yes = yes_answers()
    no = no_answers()
    idk = idk_answers()


    # Creating databases
    experiment_data = df.copy()
    user_preferences = pd.DataFrame()

    # Tkinter
    window = Tk()

    fontStyle = tkFont.Font(family="Helvetica", size=16)
    messages = Text(window, font=fontStyle)
    messages.pack()

    input_user = StringVar()
    input_field = Entry(window, text=input_user, font=fontStyle)
    input_field.pack(side=BOTTOM, fill=X)

    # Introduction
    introduction = introduction_lastfm(behaviour, ask = (input_function == text_input))
    display(introduction, "introduction.xml", networking, behaviour, messages)
    intro = True
    username = "User"

    # First question use already computed variables
    X = get_X(experiment_data)
    v = choose_randomly(X, first_variables, randomness)


    def Enter_pressed(event):
        global experiment_data
        global question_amount
        global user_preferences
        global username
        global intro
        global questions
        global v

        input_get = input_field.get()
        print(input_get)
        messages.insert(INSERT, '%s\n' % input_get)
        input_user.set('')

        # Introduction
        if intro :
            intro = False

            if behaviour == "WARM" :
                username = input_get

            # Creating question depending on the selected behaviour
            questions = behaviour_lastfm(behaviour, username)

            question = question_function(v, tags, questions)
            if len(questions) > 0:
                del questions[0]

            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages)

            return "break"

        # Switch over the user answer
        print(tags[tags.tagID == v].tagValue.iloc[0])
        print(input_get)
        if input_get in yes :
            experiment_data_ = data_without_v(experiment_data, v, 0.5, lower=False)
        elif input_get in no :
            experiment_data_ = data_without_v(experiment_data, v, 0.5, lower=True)
        elif input_get in idk :
            experiment_data_ = data_without_v(experiment_data, v, 0.5, lower=True, cut = False)
        else:
            # Case of not understanding
            repeat = "I didn't understood your answer. Can you please repeat?"

            display(repeat, "repeat.xml", networking, behaviour, messages)
            return "break"

        if experiment_data.item.unique().size > 8 and len(get_X(experiment_data).columns) > 1:
            # Questions after the first one
            X, y = get_X(experiment_data), get_y(experiment_data)
            v, _ = random_forest(X, y, randomness = randomness)
            question = question_function(v, tags, questions)
            if len(questions) > 0:
                del questions[0]

            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages)

            len_question = len(question.split(' '))
            # time.sleep(len_question / 2)

            # First end condition : there is no more item in the database, the remaning from the previous questions are recommended
            if experiment_data_["item"].size == 0:
                user_preferences = experiment_data

                # FINISH
                recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
                display(recommendations, "recommendations.xml", networking, behaviour, messages)
                clean_directory('output')
            else:
                # There is still items in the database : it is updated for further questions
                experiment_data = experiment_data_
                user_preferences = experiment_data_
            question_amount += 1
        else:
            # Second ending condition : there is less than 8 remaining artists in the database

            # FINISH
            recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
            display(recommendations, "recommendations.xml", networking, behaviour, messages)
            clean_directory('output')

        print(experiment_data.size)
        return "break"

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
