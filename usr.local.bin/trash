#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  trash.py
# @date  2009-12-17
# @author Aroldo Souza-Leite
# @modifies 2012-05-05
'''
Renames filename to filename.Trash
'''
from __future__ import print_function
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
        os.rename(filename,filename + trash_ext)
        print('trashed:', filename,file=sys.stderr)
    return filenames

def _script():
       '''
       Invoked only if this module runs as the main script.
       '''
       trash_all(sys.argv[1:])
 
if __name__=='__main__':
   _script()

