import os
import sys
import feature
from time import time 

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

def count(str_):
    for char in str_:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
            

def count_with_stats(str_):
    n_words=0
    n_characters_no_spaces=0
    n_characters=0
    n_letters=0
    '''Function for doing stats on texts, it returns the number of characters, number of words, number of letters'''
    for char in text:
        n_characters+=1
        if char!='\n':
            n_characters_no_spaces+=1
        if char.lower() in char_dict:
            n_letters+=1
    print('Stats of the text:\n')
    print(f'Number of characters with spaces: {n_characters}\nNumber of characters without spaces: {n_characters_no_spaces}\nNumber of letters: {n_letters}\n')


if __name__ == '__main__':
    start = time()
    os.chdir(sys.path[0]+'/../test')
    with open(feature.file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    count(text)
    print(f'\nNumber of occurrencies of each letter:\n{char_dict}\n')
    if feature.stats:
        count_with_stats(text)
        print(f'Time elapsed = {(time()-start):.6f} second(s)')
    else:
        print(f'Time elapsed = {(time()-start):.6f} second(s)')

