#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  trashbin.py
# @date  2013-04-22
# @author Aroldo Souza-Leite
'''
Moves files to the trashbin.
'''
from __future__ import print_function
import sys
import os
import shutil
import re
import logging
logging.basicConfig()
logger = logging.getLogger('trashbin')
logger.setLevel(logging.DEBUG)


def trashbin_all(filenames = (), trash_ext=".Trash"):
    """
    Moves every file in the list to the trashbin.
    """

    if 'trashbin' not in os.environ:
        logger.debug("trashbin not found.")
        return 
    trashbin = os.environ['trashbin']
    for filename in filenames:
            if not os.path.exists(filename):
                print("not found:", filename)
                continue
            filename = os.path.normpath(filename)
            try:
                shutil.move(filename, trashbin)
            except shutil.Error as e:
                reexpr  = "(?P<prefix>Destination path ')"
                reexpr += "(?P<path>.*?)"
                reexpr += "(?P<suffix>' already exists)"
                reexprc = re.compile(reexpr)
                searched_message  = reexprc.search(e.message)
                path = searched_message.group('path')
                shutil.rmtree(path)
                shutil.move(filename, trashbin)
                logger.info("trashed:{f}".format(f=filename))
            return filenames

def _script():
       '''
       Invoked only if this module runs as the main script.
       '''
       trashbin_all(sys.argv[1:])
 
if __name__=='__main__':
   _script()

