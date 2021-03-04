#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  say_hello
# @date  
# @author Aroldo Souza-Leite
'''
A hello module.

The hello call is implemented in
the function say_hello.
'''
from __future__ import print_function
import os
import sys

def say_hello(person):
       '''
       produces a 'hello' string.

       >>> say_hello('Bill')
       'Hello Bill! Have a good day!'
       >>> say_hello('Mary')
       'Hello Mary! Have a good day!'
       '''
       fmt = 'Hello {0}! Have a good day!'
       result_string = fmt.format(person)
       return result_string


def customized_doctest():
       '''
       examples of doctest customization.

       >>> o = object()
       >>> o #doctest: +ELLIPSIS
       <object object at 0x...>
       '''

def _script():
       '''
       Runs if this is the main module.

       Runs doctests on the current module.
       '''
       print('running doctests on ', sys.argv[0])
       print()
       import doctest
       doctest.testmod(verbose=True)

if __name__=='__main__':
   _script()

