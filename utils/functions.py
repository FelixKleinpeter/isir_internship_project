#coding:utf-8
import os, shutil
from tkinter import *

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
