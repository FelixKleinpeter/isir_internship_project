
import os
import numpy as np
import pandas as pd
import time
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

from utils.input_reader import text_input, audio_input, yes_answers, no_answers, idk_answers
from utils.file_reader import experiment_lastfm
from utils.generator.question import question_from_v_musics, question_end_experiment
from utils.output_displayer import lastfm_output_displayer
from utils.functions import clean_directory, display, save
from utils.file_reader import read_lastfm

from precomputation.lastfm import first_variable_precomputation
from behaviour.behaviour import behaviour_lastfm, introduction_lastfm
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



    # Hourglass
    img = ImageTk.PhotoImage(Image.open("images/hourglass.jpg"))
    hourglass = Label(input_field, image = img)

    # Introduction
    introduction = introduction_lastfm(behaviour, ask = (input_function == text_input))
    display(introduction, "introduction.xml", networking, behaviour, messages)
    intro = True
    username = "User"

    # First question use already computed variables
    X = get_X(experiment_data)
    v = choose_randomly(X, first_variables, randomness)

    # True during the experiment, False after the recommendations are given
    experiment = True

    # Ending questions and answers
    end_questions = question_end_experiment()
    end_answers = []

    def process(input):
        global experiment_data
        global question_amount
        global user_preferences
        global username
        global intro
        global experiment
        global questions
        global v

        finish = False

        # Introduction
        if intro :
            intro = False

            if behaviour == "WARM" :
                username = input

            # Creating question depending on the selected behaviour
            questions = behaviour_lastfm(behaviour, username)

            question = question_function(v, tags, questions)
            if len(questions) > 0:
                del questions[0]

            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages)

            return "break"

        # Switch over the user answer
        if input in yes :
            experiment_data = data_without_v(experiment_data, v, 0.5, lower=False)
        elif input in no :
            experiment_data = data_without_v(experiment_data, v, 0.5, lower=True)
        elif input in idk :
            experiment_data = data_without_v(experiment_data, v, 0.5, lower=True, cut = False)
        else:
            # Case of not understanding
            repeat = "I didn't understood your answer. Can you please repeat?"

            display(repeat, "repeat.xml", networking, behaviour, messages)
            return "break"


        # Questions after the first one

        # Hourglass while waiting
        hourglass.pack(side = "left", fill = Y, expand = None)
        window.update()

        X, y = get_X(experiment_data), get_y(experiment_data)
        v, _ = random_forest(X, y, randomness = randomness)
        question = question_function(v, tags, questions)
        if len(questions) > 0:
            del questions[0]

        hourglass.pack_forget()

        # First end condition : there is no more item in the database, the remaning from the previous questions are recommended
        if experiment_data["item"].size == 0 or experiment_data.item.unique().size <= 8 or len(get_X(experiment_data).columns) <= 1:
            user_preferences = experiment_data
            finish = True
        else:
            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages)

            # len_question = len(question.split(' '))
            # time.sleep(len_question / 2)

            # There is still items in the database : it is updated for further questions
            user_preferences = experiment_data
            question_amount += 1


        if finish:
            # FINISH
            recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
            display(recommendations, "recommendations.xml", networking, behaviour, messages)
            clean_directory('output')
            save({"recommendation":recommendations, "username":username, "behaviour":behaviour, "question_amount":question_amount})

            # Initializing the end of the process
            experiment = False
            B_rn.pack(side = "left")
            B_ry.pack(side = "left")
            window.update()

            question = end_questions[0]
            if len(end_questions) > 0:
                del end_questions[0]

            display(question, "", False, behaviour, messages)

    def questionnary(input):
        global end_questions
        global end_answers

        end_answers.append(input)

        question = end_questions[0]
        if len(end_questions) > 0:
            del end_questions[0]

        display(question, "", False, behaviour, messages)

        if len(end_questions) == 0:
            save({"final_questions":question_end_experiment(), "end_answers":end_answers})

    def send_input(input):
        print(input)
        messages.insert(INSERT, '%s\n' % input)
        if experiment:
            process(input)
        else:
            questionnary(input)

    def Enter_pressed(event):
        input = input_field.get()
        input_user.set('')
        send_input(input)

        return "break"

    def Button_yes():
        input = "Yes"
        send_input(input)

    def Button_no():
        input = "No"
        send_input(input)

    def Button_idk():
        input = "I don't know"
        send_input(input)

    def Button_rno():
        input = "Rather no"
        send_input(input)

    def Button_ryes():
        input = "Rather yes"
        send_input(input)

    # Buttons
    B_y = Button(window, text ="Yes", command = Button_yes)
    B_y.pack(side = "left")
    B_n = Button(window, text ="No", command = Button_no)
    B_n.pack(side = "left")
    B_i = Button(window, text ="I don't know", command = Button_idk)
    B_i.pack(side = "left")

    B_rn = Button(window, text ="Rather yes", command = Button_rno)
    B_ry = Button(window, text ="Rather no", command = Button_ryes)

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
