
import numpy as np
import pandas as pd
import time
from tkinter import *

from utils.input_reader import text_input, audio_input, yes_answers, no_answers, idk_answers
from utils.file_reader import experiment_lastfm
from utils.generator.question import question_from_v_musics
from utils.generator.xml_file import xml_from_question
from utils.output_displayer import lastfm_output_displayer
from utils.network.file_sender import send_to_greta
from utils.functions import clean_directory

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

    # Introduction
    introduction = introduction_lastfm(behaviour, ask = (input_function == text_input))
    if networking:
        filename = "introduction.xml"
        xml_from_question(introduction, filename, behaviour)
        send_to_greta("output/" + filename)
    username = "User"
    if behaviour == "WARM" :
        username = input_function(introduction)
    elif behaviour == "COMP" :
        print(introduction)

    # Creating question depending on the selected behaviour
    questions = behaviour_lastfm(behaviour, username)

    #experiment_data = df.copy()

    """
    while experiment_data.item.unique().size > 8 and len(get_X(experiment_data).columns) > 1:
        X, y = get_X(experiment_data), get_y(experiment_data)
        if question_amount == 0:
            v = choose_randomly(X, first_variables, randomness)
        else:
            v, _ = random_forest(X, y, randomness = randomness)
        avg = np.mean(X[v])
        question = question_function(v, tags, questions)
        if len(questions) > 0:
            del questions[0]


        if networking:
            filename = "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml"
            xml_from_question(question, filename, behaviour)
            send_to_greta("output/" + filename)


        len_question = len(question.split(' '))
        print(question)
        # time.sleep(len_question / 2)

        while True:
            y_or_n = input_function("(y/n/idk)")

            if y_or_n in yes :
                experiment_data_ = data_without_v(experiment_data, v, avg, lower=False)
                break
            elif y_or_n in no :
                experiment_data_ = data_without_v(experiment_data, v, avg, lower=True)
                break
            elif y_or_n in idk :
                experiment_data_ = data_without_v(experiment_data, v, avg, lower=True, cut = False)
                break
            else:
                repeat = "I didn't understood your answer. Can you please repeat?"
                print(repeat)
                if networking:
                    filename = "repeat.xml"
                    xml_from_question(repeat, filename, behaviour)
                    send_to_greta("output/" + filename)


        if experiment_data_["item"].size == 0:
             user_preferences = experiment_data
             break
        else:
            experiment_data = experiment_data_
            user_preferences = experiment_data
        question_amount += 1
    """
    ####################################################


    window = Tk()

    messages = Text(window)
    messages.pack()

    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)

    d = df.copy()

    def Enter_pressed(event):
        input_get = input_field.get()
        print(input_get)
        messages.insert(INSERT, '%s\n' % input_get)
        input_user.set('')
        print(1)
        print(d.head())

        if d.item.unique().size > 8 and len(get_X(d).columns) > 1:
            X, y = get_X(d), get_y(d)
            if question_amount == 0:
                v = choose_randomly(X, first_variables, randomness)
            else:
                v, _ = random_forest(X, y, randomness = randomness)
            avg = np.mean(X[v])
            question = question_function(v, tags, questions)
            if len(questions) > 0:
                del questions[0]


            if networking:
                filename = "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml"
                xml_from_question(question, filename, behaviour)
                send_to_greta("output/" + filename)


            len_question = len(question.split(' '))
            print(question)
            # time.sleep(len_question / 2)



            if input_get in yes :
                d_ = data_without_v(d, v, avg, lower=False)
            elif input_get in no :
                d_ = data_without_v(d, v, avg, lower=True)
            elif input_get in idk :
                d_ = data_without_v(d, v, avg, lower=True, cut = False)
            else:
                repeat = "I didn't understood your answer. Can you please repeat?"
                print(repeat)
                if networking:
                    filename = "repeat.xml"
                    xml_from_question(repeat, filename, behaviour)
                    send_to_greta("output/" + filename)


            if d_["item"].size == 0:
                 user_preferences = d

                 # FINISH
                 recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
                 if networking:
                     filename = "recommendations.xml"
                     xml_from_question(recommendations, filename, behaviour)
                     send_to_greta("output/" + filename)
                 print(recommendations)

                 clean_directory('output')
            else:
                d = d_
                user_preferences = d
            question_amount += 1
        else:
            # FINISH
            recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
            if networking:
                filename = "recommendations.xml"
                xml_from_question(recommendations, filename, behaviour)
                send_to_greta("output/" + filename)
            print(recommendations)
            #print("Question amount %s " % question_amount)

            clean_directory('output')


        return "break"

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()



    ####################################################
