#!/usr/bin/python3
"""This module defines a scrip that takes an argument 2 strings"""

from sys import argv, stderr
from os.path import exists

if __name__ == "__main__":

    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)

    if not exists(argv[1]):
        print(f"Missing {argv[1]}", file=stderr)
        exit(1)

    with open(argv[1], 'r', encoding='utf-8') as file:
        newFile = open("README.html", "w")
        for line in file:
            nbhash = line.count("#")
            line = line.lstrip('# ').lstrip('/n')
            newFile.write(f'<h{nbhash}>{line.rstrip()}</h{nbhash}>\n')

    exit(0)
