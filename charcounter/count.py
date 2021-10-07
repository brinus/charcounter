''' This module is the main file, providing the function count().
'''

import os
import sys
from time import time
import logging

import matplotlib.pyplot as plt

import feature

char_dict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

def settings():
    os.chdir(sys.path[0]+'/../test')
    try:
        with open(feature.file_name, 'r', encoding='utf-8') as file:
            text = file.read()
    except IOError:
        logging.error('File not found, check file name or absolute path if provided')
        return None
    return text

def count(str_):
    n_characters = 0
    for char in str_:
        n_characters += 1
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
    for key in char_dict:
        print(f'{key} : {(char_dict[key]/n_characters):.5f}')
    return

def count_with_stats(str_):
    # n_words=0
    n_characters_no_spaces=0
    n_characters=0
    n_letters=0
    '''Function for doing stats on texts, it returns the number of characters, \
        number of words, number of letters'''
    for char in str_:
        n_characters += 1
        if char != '\n':
            n_characters_no_spaces += 1
        if char.lower() in char_dict:
            n_letters += 1
            char_dict[char.lower()] += 1
    for key in char_dict:
        print(f'{key} : {(char_dict[key]/n_characters):.5f}')
    print(f'''Stats of the text:
    Number of characters with spaces: {n_characters}
    Number of characters without spaces: {n_characters_no_spaces}
    Number of letters: {n_letters}
''')

def hist_plot():
    if feature.plot_type is not None:
        _, ax = plt.subplots(1,1)
        if feature.plot_type == 'alphabetic':
            ax.bar(char_dict.keys(), char_dict.values())
        if feature.plot_type == 'decreasing':
            char_dict_sorted = {k: v for k, v in sorted(char_dict.items(), \
                key=lambda item: item[1], reverse=True)}
            ax.bar(char_dict_sorted.keys(), char_dict_sorted.values())
        plt.show()
    return

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
