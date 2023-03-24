#!/usr/bin/python3
"""
markdown2html.py - Convert a markdown file to HTML format.

Usage: ./markdown2html.py input.md output.html

This script reads a markdown file and writes an HTML file with the same content, but formatted as HTML.
It supports headings, unordered lists, and paragraphs.
"""

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
    with open(argv[2], "w", encoding='utf-8') as html:
        nextLine = file.readline()
        while nextLine:
            nbhash = nextLine.count("#")
            unorderList = nextLine.strip("- ").rstrip()
            if nbhash != 0:
                line = nextLine.lstrip('# ').lstrip('/n')
                html.write(f'<h{nbhash}>{line.rstrip()}</h{nbhash}>\n')
            if '-' in nextLine:
                html.write('<ul>\n')
                html.write(f'<li>{unorderList}</li>\n')
                nextLine = file.readline()
                while nextLine.strip().startswith('-'):
                    html.write(f'<li>{nextLine.strip("- ").rstrip()}</li>\n')
                    nextLine = file.readline()
                html.write('</ul>\n')
            else:
                nextLine = file.readline()
    exit(0)
