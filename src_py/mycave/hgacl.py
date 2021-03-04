#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  hgacl.py
# @date  2012-08-24
# @author Aroldo Souza-Leite
'''
short description

long description
long description
'''
# singular imports from __future__
from __future__ import print_function
#
import os
import sys
# a very simple pre-cofingured logger
from lb.slog import get_slog
_logger = get_slog()


def branches():
    '''
    Reads branches and permissions from an hgrc.
    '''
    info = {'willi':['willi.a', 'willi.b'],
            'rosi':['rosi.a','rosi.b']}
    return info

def _script():
       '''
       Intended to be invoked if this module is called as a script.
       '''
       pwd = os.getcwd()
       filename = os.path.basename(sys.argv[0])
       msg = 'running ' + filename + ' in ' + pwd
       _logger.info(msg)

if __name__=='__main__':
   _script()

