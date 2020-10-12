
import os
import numpy as np
import pandas as pd
import time
import tkinter as tk
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
    networking = True

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
    window = tk.Tk()
    window.title("Interactive recommendation system")

    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    fontStyle = tkFont.Font(family="Helvetica", size=16)
    messages = tk.Text(window, state='disabled', font=fontStyle, yscrollcommand = scrollbar.set)
    messages.pack()

    scrollbar.config(command=messages.yview)

    input_user = tk.StringVar()
    input_field = tk.Entry(window, text=input_user, font=fontStyle)
    #input_field.pack(side=BOTTOM, fill=X)

    # Hourglass
    img = ImageTk.PhotoImage(Image.open("images/hourglass.jpg"))
    hourglass = tk.Label(input_field, image = img)

    # Introduction
    introduction = introduction_lastfm(behaviour)
    intro = True
    username = "User"

    # First question use already computed variables
    X = get_X(experiment_data)
    v = choose_randomly(X, first_variables, randomness)

    # True during the experiment, False after the recommendations are given and during the taste questions
    experiment = False

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

            for b in initial_buttons:
                button_dict[b].pack(side = "left")

            if behaviour == "WARM" :
                username = input

            # Creating question depending on the selected behaviour
            questions = behaviour_lastfm(behaviour, username)

            question = question_function(v, tags, questions)
            if len(questions) > 0:
                del questions[0]

            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages, question_amount, str(tags[tags.tagID == v].tagValue.iloc[0]))
            question_amount += 1

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
        hourglass.pack(side = "left", fill = tk.Y, expand = None)
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
            display(question, "question_about_" + str(tags[tags.tagID == v].tagValue.iloc[0]) + ".xml", networking, behaviour, messages, question_amount, str(tags[tags.tagID == v].tagValue.iloc[0]))

            # len_question = len(question.split(' '))
            # time.sleep(len_question / 2)

            # There is still items in the database : it is updated for further questions
            user_preferences = experiment_data
            question_amount += 1


        if finish:
            # FINISH
            recommendations = lastfm_output_displayer(user_preferences, artists, behaviour)
            display(recommendations, "recommendations.xml", networking, behaviour, messages, variable = "recommendations")
            clean_directory('output')
            save({"recommendation":recommendations, "username":username, "behaviour":behaviour, "question_amount":question_amount}, "result")

            # Initializing the end of the process
            experiment = False
            for b in initial_buttons:
                button_dict[b].pack_forget()
            for b in ending_buttons:
                button_dict[b].pack(side = "left")
            window.update()
            input_field.pack_forget()

            question = end_questions[0]
            if len(end_questions) > 0:
                del end_questions[0]

            display(question, "", False, behaviour, messages)

    def questionnary(input):
        global end_questions
        global end_answers
        global experiment
        global input_field

        end_answers.append(input)

        if len(end_questions) == 0:
            save({"final_questions":question_end_experiment(), "end_answers":end_answers}, "answers")
            display("Thank you!", "", networking, False, messages)
            window.update()
            time.sleep(3)
            window.destroy()
        else:
            if len(end_questions) < 15 and intro:
                for b in ending_buttons:
                    button_dict[b].pack_forget()
                for b in start_buttons:
                    button_dict[b].pack(side = "left")
            if len(end_questions) < 14 and intro:
                experiment = True
                display(introduction, "introduction.xml", networking, behaviour, messages, variable = "introduction")
                for b in start_buttons:
                    button_dict[b].pack_forget()

                input_field.pack(side=tk.BOTTOM, fill=tk.X)
            else:
                question = end_questions[0]
                display(question, "", False, behaviour, messages)
                del end_questions[0]



    def send_input(input):
        print(input)

        # Change the state allow to write on the read only window
        messages.configure(state='normal')
        messages.insert(tk.INSERT, '> %s\n' % input)
        messages.tag_add("start", "insert - 1l", "insert")
        messages.tag_config("start", background="white", foreground="gray44")
        messages.configure(state='disabled')

        if experiment:
            process(input)
        else:
            questionnary(input)

    def Enter_pressed(event):
        input = input_field.get()
        input_user.set('')
        send_input(input)

        return "break"

    def button(input):
        send_input(input)

    # Buttons
    initial_buttons = ["Yes", "I don't have a preference", "No"]
    ending_buttons = ["Not at all", "Somewhat Disagree", "Neither Agree nor Disagree", "Somewhat Agree", "Completely Agree"]
    # Most popular : rock, pop, alternative, electronic, indie, female vocalist, 80s, dance, alternative rock, classic rock, british, indie rock, singer-songwritter, hard rock, experimental, metal
    start_buttons = ["Start"]
    # A loop doesn't work because the iterator will change and functions won't work
    button_dict = {
        "Yes":tk.Button(window, text = "Yes", command = lambda: button("Yes"), width=20, height=2),
        "I don't have a preference":tk.Button(window, text = "I don't have a preference", command = lambda: button("I don't have a preference"), width=20, height=2),
        "No":tk.Button(window, text = "No", command = lambda: button("No"), width=20, height=2),
        "Completely Agree":tk.Button(window, text = "Completely Agree", command = lambda: button("Completely Agree"), width=20, height=2),
        "Somewhat Agree":tk.Button(window, text =  "Somewhat Agree", command = lambda: button( "Somewhat Agree"), width=20, height=2),
        "Neither Agree nor Disagree":tk.Button(window, text = "Neither Agree nor Disagree", command = lambda: button("Neither Agree nor Disagree"), width=20, height=2),
        "Somewhat Disagree":tk.Button(window, text = "Somewhat Disagree", command = lambda: button("Somewhat Disagree"), width=20, height=2),
        "Not at all":tk.Button(window, text = "Not at all", command = lambda: button("Not at all"), width=20, height=2),
        "Start":tk.Button(window, text = "Start", command = lambda: button("Start"), width=20, height=2),
    }

    # Introduce the first sentence
    question = end_questions[0]
    display(question, "", False, behaviour, messages)
    del end_questions[0]
    for b in ending_buttons:
        button_dict[b].pack(side = "left")



    frame = tk.Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()
