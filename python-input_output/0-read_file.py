#!/usr/bin/python3
""" read file func"""

def read_file(filename=""):
    """ Read a file using `with` statement"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')