import os
import sys

def count(str_):
    pass

if __name__ == '__main__':
    os.chdir(sys.path[0]+'/..')
    file_name = str(input())
    with open(file_name, 'r') as file:
        text = file.read()
    print(text)
