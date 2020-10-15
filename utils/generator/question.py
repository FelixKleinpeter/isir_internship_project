# coding:utf-8

def question_from_v_movies(variable, threshold=0):
    try:
        if len(question_dict[variable]) == 0:
            return "Do you like " + variable + " movies? (y/n)"
        if threshold <= 1:
            return question_dict[variable]
        return question_dict[variable] + str(threshold) + "? (y/n)"
    except:
        return str(variable) + "? (y/n)"

def question_from_v_musics(variable, tags, questions=[]):
    if len(questions) == 0:
        return "Do you like " + str(tags[tags.tagID == variable].tagValue.iloc[0]) + " music?"
    else:
        question = questions[0]
        words = question.split(" ")
        new_words = [str(tags[tags.tagID == variable].tagValue.iloc[0]) if w == "*" else w for w in words]
        new_question = " "
        return new_question.join(new_words)

def question_end_experiment():
    return [ "During this experiment, an agent will ask you some questions about your music taste. Before starting, we would like to have a quick overview of them. We will give you some sentences, and you will have to say if you agree or disagree with them, on a five degree scale from \"Not at all\" to \"Completely\". \n\nYou enjoy listening to music.",
        "Our database contains a majority of English-speaking artists from the last seven decades. Are there any artists of this period you appreciate?",
        "If not, please answer as if you were interested in discovering some of them. The experiment will start now. Please press any button when you are ready to start.",
        "\n================================ QUESTIONNARY =================================\n\nIt is the end of the experiment. Again, we will give you some sentences, and you will have to say if you agree or disagree with them, on a five degree scale from \"Not at all\" to \"Completely\". \n\nThere are artists you recognize in the recommendations.",
        "The questions asked by Alice are intelligent.",
        "Alice is friendly.",
        "You are interested in listening to the music recommended by Alice.",
        "Alice's recommendations are trustworthy.",
        "Alice looks capable.",
        "You are satisfied with the recommendations.",
        "Alice's behavior is aggressive.",
        "You feel that Alice is well-intended.",
        "Alice doesn't look qualified for her task.",
        "Alice is warm.",
        "The recommendations align with your expectations.",
        "You have confidence in Alice.",
        ]
