# coding:utf-8

def behaviour_lastfm(behaviour, username):
    questions = []
    if behaviour == "WARM":
        questions.append("Let's start, " + username + "! What do you think about * music? Do you like it?")
        questions.append("Then, do you enjoy listening to * music?")
        questions.append("I'm wondering if you like * music?")
        questions.append("Mmh, what about * music then?")
        questions.append("And about * music?")
        questions.append("I think I'm close to find new artists for you! Tell me, "+username+", do you like * music?")
        questions.append("And what about * music?")
    elif behaviour == "COMP":
        questions.append("Do you often listen to * music?")
        questions.append("The next question will be about * music. Do you listen to it?")
        questions.append("Do you like * music?")
        questions.append("Then, * music?")
        questions.append("Do you listen to * music?")
        questions.append("We are reaching the end of the experiment. Do you like * music?")
    return questions

def introduction_lastfm(behaviour):
    if behaviour == "WARM":
        return "Nice to meet you! I would like to ask you some questions about your music taste to find new artists to recommend. I'm Camille, what is your name?"
    elif behaviour == "COMP":
        return "Hello, user. I will ask you questions about your music taste to recommend you new artists. Are you ready to start?"
    return ""
