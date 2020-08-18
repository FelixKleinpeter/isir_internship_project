#coding:utf-8
import speech_recognition as sr

def text_input(question):
    answer = input(question+"\n")
    return answer

def audio_input(question):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(question)
        audio = r.record(source, duration=4)

    answer = ""
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        answer =  r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return answer

def yes_answers():
    return ["y", "Y", "yes", "Yes"]

def no_answers():
    return ["n", "N", "no", "No"]

def idk_answers():
    return ["idk", "Idk", "I don't know", "i don't know"]
