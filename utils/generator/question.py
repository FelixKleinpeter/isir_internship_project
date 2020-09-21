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
    return [ "Is there one or more artists you already know in these recommendations?",
        "If there are artists you don't know, would you like to check for these artists?",
        "Are these recommendations aligned with your expectations? ",
        "Are you satisfied with these recommendations?",
        "During the experiment, did you feel that the agent was well-intended?",
        "Did you feel that the agent was trustworthy?",
        "Did you have confidence in the agent?",
        "Did the agent think that the agent was asking intelligent questions?",
        "Did the agent look capable?",
        "Do you think that the agent was irrelevant?",
        "Did the agent give you a bad feeling?",
        "Did you feel that the agent was sympathetic?",
        "Was the agent warm?"]
