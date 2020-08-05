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

def question_from_v_musics(variable, tags=None):
    return "Do you like " + str(tags[tags.tagID == variable].tagValue.iloc[0]) + " music?"
