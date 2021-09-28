import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file to be analized must be in plain text format (.txt), it can be placed in /test folder or called with the absolute path.')
args = parser.parse_args()
file_name = args.file_name
