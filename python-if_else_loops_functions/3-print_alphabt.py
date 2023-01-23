#!/usr/bin/python3
for lower in range(97, 123):
    if lower == ord('q') or lower == ord('e'):
        continue
    print("{:c}".format(lower), end="")
