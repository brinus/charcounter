''' This module is the main file, providing the function that counts \
    the relative frequency of each letter and prints it. It is done  \
    in function count() and count_with_stats(), depending on the     \
    choice of the user. Type -h for seeing the options.
'''

import os
import sys
from time import time
import logging
import string

import matplotlib.pyplot as plt

import feature

# pylint: disable = invalid-name

char_dict = {key : 0 for key in string.ascii_lowercase}

def settings():
    ''' settings() is used for reading the file.txt, with the use
        of the library os. it takes as input the name with or
        without its absolute path. If the file.txt is in the
        folder test, the path is not needed.
        If the file cannot be found, it returns a specific message.
    '''
    os.chdir(sys.path[0]+'/../test')
    try:
        with open(feature.file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError:
        logging.error('File not found, check file name or absolute path if provided')
        return None

def count(str_):
    ''' count() takes the text as an input and calculates the relative
        frequency of each letter. Then it prints the results.
    '''
    n_characters = 0
    for char in str_:
        n_characters += 1
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
    for key, value in char_dict.items():
        print(f'{key} : {(value / n_characters):.5f}')

def count_with_stats(_str):
    ''' count() takes the text as an input and calculates the relative  \
    frequency of each letter and other stats on the text.          \
    Then it prints the results.
    '''
    n_words=0
    flag=0
    n_characters_no_spaces=0
    n_characters=0
    n_letters=0
    for char in _str:
        n_characters += 1
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
            n_letters+=1
            n_characters_no_spaces+=1
            flag=1
        elif char != ' ':
            n_characters_no_spaces += 1
        elif flag == 1:
            n_words += 1
            flag=0

    for key in char_dict:
        print(f'{key} : {(char_dict[key]/n_characters):.5f}')
    print(f'''Stats of the text:
    Number of characters with spaces: {n_characters}
    Number of characters without spaces: {n_characters_no_spaces}
    Number of letters: {n_letters}
        Number of words: {n_words}
''')

def hist_plot():
    ''' hist_plot() creates the histogram of the frequency of the text.\
    It plots in alphabetic or decreasing order. If anything is     \
    specified by the user, alphabetic order is used. For seeing how\
    to choose the order, type -h.
    '''
    if feature.plot_type is not None:
        _, ax = plt.subplots(1,1)
        if feature.plot_type == 'alphabetic':
            ax.bar(char_dict.keys(), char_dict.values())
        if feature.plot_type == 'decreasing':
            char_dict_sorted = dict(sorted(char_dict.items(), key=lambda item: \
                item[1], reverse=True))
            ax.bar(char_dict_sorted.keys(), char_dict_sorted.values())
        plt.show()

if __name__ == '__main__':
    start = time()
    text = settings()
    if text is not None:
        if feature.stats:
            count_with_stats(text)
            print(f'Time elapsed = {(time()-start):.6f} second(s)')
        else:
            count(text)
            print(f'Time elapsed = {(time()-start):.6f} second(s)')
        hist_plot()
