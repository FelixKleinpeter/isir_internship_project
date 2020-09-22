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
    return [ "\nIt is the end of the experiment. We will give you some sentences, and you will have to say if you agree or disagree with them, on a five degree scale from \"Not at all\" to \"Completely\". \n\nYou like to listen to music offently.",
        "Among the music of the last century, there are lot of artists you like.",
        "There are artists you already know in these recommendations.",
        "You will check for the artists you don't know.",
        "These recommendations aligned to your expectations.",
        "You are satisfied with the recommendations.",
        "You feel that the agent is well-intended.",
        "The agent is truthworthy.",
        "You have confidence in the agent.",
        "The questions of the agent were intelligent.",
        "The agent look capable.",
        "The agent is irrelevant.",
        "The agent gives you a bad feeling.",
        "The agent is sympathic.",
        "The agent is warm."]
