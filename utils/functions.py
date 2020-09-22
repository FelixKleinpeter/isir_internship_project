#coding:utf-8
import os, shutil
from tkinter import *
import pickle

from utils.generator.xml_file import xml_from_question
from utils.network.file_sender import send_to_greta

def clean_directory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def display(sentence, filename, networking, behaviour, messages):
    print(sentence)
    # Change the state allow to write on the read only window
    messages.configure(state='normal')
    messages.insert(INSERT, '%s\n' % sentence)
    messages.configure(state='disabled')
    messages.see("end")
    if networking:
        xml_from_question(sentence, filename, behaviour)
        send_to_greta("output/" + filename)

def save(dictionnary, name):
    # Save a dictionnary of elements under the name "result_x" where x is the number in the "count.txt" file. Increase the number in this file.
    count_file = open("results/count.txt", "r")
    count = int(count_file.read())
    while os.path.exists("results/"+name+str(count)+".p"):
        count_file = open("results/count.txt", "w")
        count += 1
        count_file.write(str(count))

    pickle.dump( dictionnary, open( "results/"+name+str(count)+".p", "wb" ) )
