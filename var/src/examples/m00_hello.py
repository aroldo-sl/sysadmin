#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  m00_hello.py
# @date  2012-05-04
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

def _script():
       '''
       Intended to be invoked if this module is called as a script.
       '''
       pwd = os.getcwd()
       filename = os.path.basename(sys.argv[0])
       msg = 'running ' + filename + ' in ' + pwd
       print(msg, file=sys.stderr)

if __name__=='__main__':
   _script()

