# coding:utf-8

def behaviour_lastfm(behaviour, username):
    questions = []
    if behaviour == "WARM":
        questions.append("Let's start, " + username + "! What do you think about * music? Do you like it?")
        questions.append("Then, do you enjoy listening to * music?")
        questions.append("Mmmmh, what about * music then?")
        questions.append("And about * music?")
        questions.append("Then, maybe you like to listen to * music?")
        questions.append("I think I'm close to find new artists for you! Tell me, "+username+", do you like * music?")
        questions.append("And what about * music?")
    elif behaviour == "COMP":
        questions.append("Do you often listen to * music?")
        questions.append("Then, do you listen to * music?")
        questions.append("Do you like * music?")
        questions.append("Then, * music?")
        questions.append("Do you listen to * music?")
        questions.append("We are reaching the end of the experiment. Do you like * music?")
    return questions

def introduction_lastfm(behaviour, ask = False):
    if behaviour == "WARM":
        s = "Nice to meet you! I would like to ask you some questions about your music taste to find new artists to recommend. After each of your answers, I will try to find the best question to find what to recommend to you as fast as possible! "
        if ask :
            s += "I'm Camille, what is your name?"
        return s
    elif behaviour == "COMP":
        s = "Hello, user. Our purpose is to ask questions about music tastes to recommend new artists. After each answer, we find the next question to ask to reduce the total amount of questions. "
        return s
    return ""
