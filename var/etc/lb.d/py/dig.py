#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  dig.py
# @date  2012-11-26
# @author Aroldo Souza-Leite
'''
Parses command line values and prints them out to the standard ouput.
'''
############################## <module boilerplate> ########################################
from __future__ import print_function
import os
import  sys
import subprocess
def _basic_logger(name = None, 
                  level = None, # default: logging.DEBUG
                  stream = sys.stderr,
                 ):
    '''
    A logger from a 'logging' basic configuration.
    
    A simple but more flexible logger can 
    be imported from the package lb.slog.

    @return slog : a basic configured logger.
    '''
    # default name
    if name is None:
        import time
        name = sys.argv[0]
        name = os.path.splitext(name)[0]
        name = name + '.' + str(time.time())
    import logging
    if level is None:
        level = logging.DEBUG
    logging.basicConfig()
    slog = logging.getLogger(name)
    from logging import StreamHandler
    handler = StreamHandler(stream)
    slog.setLevel(level)
    return slog
slog = _basic_logger()
############################## </module boilerplate> ########################################

import argparse
def _parse_cli_arguments():
    '''
    Parses the command line arguments.

    @return args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-x',
                        '--x-values', 
                        help = 'Some values.',
                        metavar = 'X',
                        nargs = '+',
                        dest = 'x',
                        )
    args = parser.parse_args()
    return args


def _script():
       '''
       Intended to be invoked if this module is called as a script.
       '''
       slog.info("starting")
       args = _parse_cli_arguments()
       for  entry in args.x:
            print(entry)

if __name__=='__main__':
   _script()

