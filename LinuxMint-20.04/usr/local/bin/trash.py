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

def trash_all(filenames = (), trash_ext=".Trash"):
    """
    Trashes every file in the list.
    """
    for filename in filenames:
        if not os.path.exists(filename):
            print("not found:", filename)
            continue
        filename = os.path.normpath(filename)
        filename_Trash = filename + trash_ext
        if os.path.exists(filename_Trash):
            print("{filename} already trashed.".format(filename=filename) )
            continue
        os.rename(filename, filename + trash_ext)
        print('trashed:', filename, file=sys.stderr)
    return filenames

def _script():
       '''
       Invoked only if this module runs as the main script.
       '''
       trash_all(sys.argv[1:])
 
if __name__=='__main__':
   _script()

