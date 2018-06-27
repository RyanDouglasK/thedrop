#!/usr/bin/python


import argparse

parser = argparse.ArgumentParser(description='Which word is longer')
parser.add_argument('firstword')
parser.add_argument('secondword')

args = parser.parse_args()

if len(args.firstword) > len(args.secondword):
    print(args.firstword)
elif len(args.secondword) > len(args.firstword):
    print(args.secondword)
else:
    print('They are the same length!')
