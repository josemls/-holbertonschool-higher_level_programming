#!/usr/bin/python3
"""_summary_"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    file = load_from_json_file("add_item.json")
except:
    file = []
for i in sys.argv[1:]:
    file.append(i)
save_to_json_file(file, "add_item.json")