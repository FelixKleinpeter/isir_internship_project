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
    messages.insert(INSERT, '%s\n' % sentence)
    if networking:
        xml_from_question(sentence, filename, behaviour)
        send_to_greta("output/" + filename)

def save(dictionnary):
    # Save a dictionnary of elements under the name "result_x" where x is the number in the "count.txt" file. Increase the number in this file.
    count_file = open("results/count.txt", "r")
    count = int(count_file.read())

    count_file = open("results/count.txt", "w")
    count_file.write(str(count+1))

    pickle.dump( dictionnary, open( "results/result_"+str(count)+".p", "wb" ) )
