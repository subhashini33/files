# import required packages

from nltk import word_tokenize
import os
from collections import Counter


def read_file(file_name,mode="r"):
    """
        input file_name
        input mode "r","w","r+","w+"
        return file content a string
    """
    with open(file_name, "r",encoding="utf8") as f:
        lines = f.read()
    return lines

def read_lines(file_name,mode="r"):
    with open(file_name, "r",encoding="utf8") as f:
        lines = f.readlines()
    return lines

def lines_count(file_name):
    """
        sample function call lines_count("sample.txt")
    """
    t=read_lines(file_name) #read_lines function calling
    return len(t)

def word_count_nltk(file_name):
    t=read_file(file_name)
    res = word_tokenize(t)
    l2 = []    
    for word in res:
        l2 += word
    return len(l2)

def word_preprocess(word):
    """ Hello -->hello
        python, -->python
        (name) -->name
        " " --> None
    """
    # output should be cleaned word return None if you want to to remove the word

    return
def get_words_preprocess(words):

    return words

def get_word_count():
    
    return count

def get_file_paths(folder_path):
    """return list of files in folder or subfolders"""
    return

def get_unique_words(path):
    """
        input - either a folder or file
        output - unique words in fi;e or folder

    """
    return unique_words

def get_word_frequency(path):
    """
    """
    return 








    




