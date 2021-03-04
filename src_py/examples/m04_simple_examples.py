#!python
# -*- coding: cp1252 -*-
#
# @file  m04_simple_examples.py
# @date  2012-04-23
# @author Aroldo Souza-Leite
'''
Some simple syntax examples.

Also with the purpose of testing
the Sphinx autodoc feature. See the
Sphinx documentation.
'''
from __future__ import print_function
import sys
from m01_hello import say_hello
# 2. import version:
# import m01_hello
# or
# import examples.m01_hello (von weiter weg)

def hello_luebeck():
    '''
    Ein erstes Hallo von Luebeck.
    '''
    return "Hallo aus Luebeck!!"

def use_say_hello():
    '''
    Beispiel der Benutzung einer importierten Funktion.
    '''
    # 1. import version (if the funcitions was imported from m01_hello)
    text = say_hello()
    # 2. import version (if the module m01_hello was imported)
    # text = m01_hello.say_hello()

    return text.upper()
     
def _script():
       '''
       Intended to be invoked if this module is called as a script.
       '''
       print('running ', sys.argv[0]) 

        
if __name__=='__main__':
   _script()

