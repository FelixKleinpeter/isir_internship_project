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
