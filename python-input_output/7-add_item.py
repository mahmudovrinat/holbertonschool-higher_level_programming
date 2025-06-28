#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list,
then saves them to a file as JSON representation using
functions from 5-save_to_json_file.py and 6-load_from_json_file.py.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    try:
        # Yüklə mövcud siyahını fayldan
        items = load_from_json_file(filename)
    except FileNotFoundError:
        # Fayl yoxdursa, boş siyahı yaradılır
        items = []

    # Komanda sətri arqumentlərini (ilk arqument skriptin özüdür, onu atırıq)
    args = sys.argv[1:]
    # Yeni arqumentləri mövcud siyahıya əlavə edirik
    items.extend(args)

    # Yenilənmiş siyahını JSON fayla yazırıq
    save_to_json_file(items, filename)
