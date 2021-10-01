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
    return

def hist_plot():
    if feature.plot_type is not None:
        _, ax = plt.subplots(1,1)
        if feature.plot_type == 'alphabetic':
            ax.bar(char_dict.keys(), char_dict.values())
        if feature.plot_type == 'decreasing':
            char_dict_sorted = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}
            ax.bar(char_dict_sorted.keys(), char_dict_sorted.values())
        plt.show()
    return

if __name__ == '__main__':
    start = time()
    os.chdir(sys.path[0]+'/../test')
    with open(feature.file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    count(text)
    print(char_dict)
    print(f'Time elapsed = {(time()-start):.6f} second(s)')
    hist_plot()
