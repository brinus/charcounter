''' This module provides implementations for command line options, argparse     \
    library is used in order to achieve that. See argparse documentations at:   \
        https://docs.python.org/3/library/argparse.html    
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file to be analized must be in plain \
    text format (.txt), it can be placed in /test folder or called with its abso\
        lute path.')
parser.add_argument('-p', '--plothist', nargs='?', default=None, const='alphabet\
    ic', choices=['alphabetic', 'decreasing'], help='[ORDERING] = [alphabetic, d\
    ecreasing] \nEnables histogram plot. The user can specify if the histogram b\
    ar must be ordered in values-decreasing order or alphabetic-keys order. If n\
    othing is passed to -p/--plothist, the default choice is alphabetic ordering\
    .', metavar=('ORDERING'))
parser.add_argument("-s","--stats",help='Prints on terminal the stats of the book',action="store_true")

args = parser.parse_args()
file_name = args.file_name
plot_type = args.plothist
stats = args.stats
