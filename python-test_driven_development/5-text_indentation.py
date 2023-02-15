#!/usr/bin/python3
""" Function that print a text"""


def text_indentation(text):
        """ Function that print a text with 2 new lines after
         each of these characters: ., ? and :
        Args:
                text (str): text to print
        Raises:
                TyperError: if text is not string
        """
        if type(text) is not str:
                raise TypeError("text must be a string")
        aux = 1
        for c in text:
                if aux == 1 and c == ' ':
                        continue
                aux = 0
                print(c, end='')
                if c in [':', '?', '.']:
                        aux = 1
                        print("\n")
