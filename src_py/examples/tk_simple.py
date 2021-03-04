<<<<<<< local
<<<<<<< local
=======
>>>>>>> other
#!python
<<<<<<< local
=======
#! /usr/bin/env python
>>>>>>> other
# -*- coding: utf-8 -*-
=======
# -*- coding: cp1252 -*-
>>>>>>> other
#
# @file  tk_simple.py
# @date  2011-05-17
# @author Aroldo Souza-Leite
'''
Some very simple GUI Tkinter based utilities.
'''
from __future__ import print_function

# this is a Python 2.7 module.
import Tkinter as tkinter

# for Python 3:
# import tkinter

def tk_readstring(title='input window',
                  geometry="200x80+200+200",
                  prompt="input:",
                  ):
       '''
       A simple Tk window for reading a string.

       Returns the string from the
       string input field.

       Finish with 'RETURN' or click
       on 'Ok'.
       '''
       root =tkinter.Tk()
       root.title(title)
       #root.geometry("500x80+200+200")
       root.geometry(geometry)
       label = tkinter.Label(root,
                             text=prompt)
       label.pack()
       entry=tkinter.Entry(root)
       entry.pack()
       entry.focus_set()
       button = tkinter.Button(root,
                               text='Ok')
       button.pack()
       s=['']
       def ready(event):
              s[0] =entry.get()
              root.destroy()
       button.bind('<Button-1>', ready)
       root.bind('<Return>', ready)
       root.mainloop()

       return s[0]


def tk_message(title='message window',
               geometry="200x80+200+200",
               message="Hello from TK:",
                  ):
       '''
       Displays a message in a Tk window.
       '''
       root =tkinter.Tk()
       root.title(title)
       #root.geometry("500x80+200+200")
       root.geometry(geometry)
       label = tkinter.Label(root,
                             text=message)
       label.pack()
       button = tkinter.Button(root,
                               text='Ok')
       button.pack()
       button.focus_set()
       def ok(event):
              root.destroy()
       button.bind('<Button-1>', ok)
       root.bind('<Return>', ok)
       root.mainloop()

       return None


def _script():
       '''
       Invoked only if this module runs as the main script.
       '''
       input_string= \
           tk_readstring(prompt="some input please:")
       tk_message(message="your input was {0} ".format(input_string))
       

if __name__=='__main__':
   _script()

