<<<<<<< local
<<<<<<< local
=======
>>>>>>> other
#!python
<<<<<<< local
=======
#!/usr/bin/env python
>>>>>>> other
# -*- coding: utf-8 -*-
=======
# -*- coding: cp1252 -*-
>>>>>>> other
#
# @file  m00_module_template.py
# @date  2012-04-16
# @author Aroldo Souza-Leite
'''
The first inline doc part is only one short line.

The second part of the inline doc
can be long and have many paragraphs.
'''
# Singular, very untypical imports from __future__
# It is a backport of some features from Python3 to Python2 
from __future__ import print_function
# Don't learn the import syntax above. In general, it is wrong syntax
#
import os
import sys

def _module_info():
    '''
    Some system information about this module.
    '''
    # using the Python3 print function
    # using the os (operating system) module
    # using the sys (Python system) module
    print('file name:', os.path.basename(sys.argv[0]))
    print('current work directory:', os.getcwd())
    print('Python executable:', sys.executable)
    print()

def _script():
    '''
    Intended to be invoked if this module is called as a script.
    '''
    _module_info()

if __name__=='__main__':
   _script()

