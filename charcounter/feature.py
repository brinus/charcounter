''' This module provides implementations for command line options, argparse     \
    library is used in order to achieve that. See argparse documentations at:   \
        https://docs.python.org/3/library/argparse.html    
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file to be analized must be in plain \
    text format (.txt), it can be placed in /test folder or called with its abso\
        lute path.')
args = parser.parse_args()
file_name = args.file_name
