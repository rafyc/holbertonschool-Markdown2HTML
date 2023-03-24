#!/usr/bin/python3

from sys import argv
from os.path import exists

if __name__ == "__main__":
    if len (argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if not exists(argv[1]):
        print(f"Missing {argv[1]}")
        exit(1)
    else
    exit(0)
