#!/usr/bin/python3
"""Module define funct to load, add, save"""


from sys import argv


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        save_to_json_file(load_from_json_file(FILENAME) + argv[1:], FILENAME)
    except (FileNotFoundError, ValueError):
        save_to_json_file(argv[1:], FILENAME)
