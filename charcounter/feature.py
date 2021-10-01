import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file to be analized must be in plain text format (.txt), it can be placed in /test folder or called with its absolute path.')
parser.add_argument('-p', '--plothist', nargs='?', default=None, const='alphabetic', choices=['alphabetic', 'decreasing'], help='The user can specify if the histogram bar must be ordered in values-decreasing order or alphabetic-keys order.', metavar=('ORDERING'))
args = parser.parse_args()
file_name = args.file_name
plot_type = args.plothist
