#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  build.py
# @date  2015-06-01
# @author Aroldo Souza-Leite
"""
Help functions for Make.
"""
import os
import sys
import time
from pprint import pformat
import argparse

###### basic logging configuration
import logging
_fmt = """
%(levelname)s:[%(name)s][%(asctime)s][%(module)s.%(funcName)s]
%(message)s"""
logging.basicConfig(format = _fmt,
                    stream = sys.stderr)
slog = logging.getLogger(__name__ + str(time.time()).replace('.','_'))
slog.setLevel(logging.DEBUG)
######

def parse_args(description="Process command line arguments."):
    """
    Handles the script command line arguments.

    Returns an object 'args' with the attributes corresponding
    to the command parameters.
    """
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument(
       # arguments without a name in the command line,
       # also called positional arguments.
       'args_positional',
       # parameter name used only in the help string:
       metavar='P', 
       type=str, 
       # None,one or many parameters are required:
       nargs='*',
       help='The positional paramenters. (None, one or many)')
    args = parser.parse_args()
    return  args


def find_Makefile(start= os.path.curdir):
    """
    Finds the next Makefile.
    """
    


def _script():
       """
       Intended to be invoked if this module is called as a script.
       """
       slog.info('Parsing and displaying the command line arguments:')
       args = parse_args()
       print(args, file = sys.stderr)
       
if __name__=='__main__':
   _script()

del _script
