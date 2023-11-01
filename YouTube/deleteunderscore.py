#!/usr/bin/env python
# @file: deleteunderscore
# @date: 2023-11-01
# @modified: 
"""
Deletes underscores, spaces and other
special characters from filenames
in the current work directory.
"""
from pathlib import Path

workdir = Path.cwd()
special_characters = ("_", # urderscore
                      " ") # space
for source_filepath in workdir.iterdir():
    name = source_filepath.name
    for special_character in special_characters:
        name = name.replace(special_character, "")
    if name == source_filepath.name:
        continue
    target_filepath = source_filepath.with_name(name)
    print(source_filepath.name, target_filepath.name, sep = "\n->")
    source_filepath.rename(target_filepath)
