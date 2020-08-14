# coding:utf-8

def behaviour_lastfm(behaviour):
    questions = []
    if behaviour == "WARM":
        questions.append("Hi user, ready for some questions about your music taste? Let's start! What do you think about * music? Do you like it?")
        questions.append("Then, do you enjoy listening for * music?")
        questions.append("I'm wondering if you like * music?")
    elif behaviour == "COMP":
        questions.append("The purpose of the questions will be to find which music fit your taste. Do you often listen for * music?")
        questions.append("The next question will be about * music. Do you listen for it?")
    return questions
