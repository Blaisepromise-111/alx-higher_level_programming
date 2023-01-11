#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,
    after each line containing a specific string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file,
        after each line containing a specific string (see example):"""
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string

    with open(filename, "w") as w:
        w.write(txt)
