# coding:utf-8

def behaviour_lastfm(behaviour, username):
    questions = []
    if behaviour == "WARM":
        questions.append("Let's start, " + username + "! What do you think about * music? Do you like it?")
        questions.append("Then, do you enjoy listening to * music?")
        questions.append("Well, what about * music then?")
        questions.append("And about * music?")
        questions.append("Then, maybe you like to listen to * music?")
        questions.append("And what about * music?")
        questions.append("And about * music then?")
        questions.append("I think I'm close to find new artists for you! Tell me, "+username+", do you like * music?")
    elif behaviour == "COMP":
        questions.append("We are interested in knowing if you often listen to * music.")
        questions.append("Then, do you listen to * music?")
        questions.append("And * music?")
        questions.append("Given this, we would like to know if you appreciate * music.")
        questions.append("Do you often listen to * music?")
        questions.append("At this state of the process, we are concerned with your taste for * music. Do you often listen to it?")
        questions.append("Then, do you listen to * music?")
        questions.append("We are reaching the end of the experiment. Do you like * music?")
    return questions

def introduction_lastfm(behaviour):
    if behaviour == "WARM":
        return "Nice to meet you! I'm Alice, what is your name?"
    elif behaviour == "COMP":
        return "Hello, User, my name is Alice. Please press the Start button again when you are ready. "
    return ""
