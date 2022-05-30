#! /usr/bin/env python3
# @file  trash.py
# @date  2009-12-17
# @author Aroldo Souza-Leite
# @modified 2021-05-08
'''
Renames filename to filename.Trash
'''
import sys
import os

def trash_one(filename, trash_ext = ".Trash"):
    """
    Trashes one file or directory.
    """
    if not os.path.exists(filename):
        print("not found:", filename)
        trashed_item = (filename, None)
        return trashed_item
    filename = os.path.normpath(filename)
    filename_Trash = filename + trash_ext
    if os.path.exists(filename_Trash):
        trash_one(filename_Trash, trash_ext)
    os.rename(filename, filename_Trash)
    trashed_item = (filename, filename_Trash)
    return trashed_item


def trash_all(filenames = (), trash_ext=".Trash"):
    """
    Trashes every file in the list.
    """
    trashed_items = []
    for filename in filenames:
        trashed_item = trash_one(filename, trash_ext = trash_ext)
        trashed_items.append(trashed_item)
    return trashed_items

def _script():
       '''
       Invoked only if this module runs as the main script.
       '''
       trashed_items = trash_all(sys.argv[1:])
       for filename, filename_Trash in trashed_items:
           msg= "{filename} -> {filename_Trash}".format(
               filename = filename, filename_Trash = filename_Trash)
           print (msg)
 
if __name__=='__main__':
   _script()

