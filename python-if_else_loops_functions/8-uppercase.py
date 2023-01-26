#!/usr/bin/python3
def uppercase(str):
    for msg in str[:]:
        if ord(msg) >= 97 and ord(msg) <= 122:
            msg = chr(ord(msg) - 32)
        print("{}".format(msg), end="")
    print()
