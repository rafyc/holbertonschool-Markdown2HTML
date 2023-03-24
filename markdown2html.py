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

    exit(0)
