import os
import sys
import feature
from time import time 
import matplotlib.pyplot as plt

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

def hist_plot():
    fig, ax = plt.subplots(1,1)
    ax.bar(char_dict.keys(), char_dict.values())
    plt.show()

if __name__ == '__main__':
    start = time()
    os.chdir(sys.path[0]+'/../test')
    with open(feature.file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    count(text)
    print(char_dict)
    print(f'Time elapsed = {(time()-start):.6f} second(s)')
    hist_plot()
