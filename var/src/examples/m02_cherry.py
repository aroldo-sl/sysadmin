#!python
# -*- coding: cp1252 -*-
#
# @file  m02_cherry.py
# @date  2012-04-22
# @author Aroldo Souza-Leite
'''
Introduction to CherryPy
'''
from __future__ import print_function
import sys
import cherrypy


class HelloWorld(object):
    '''
    A class of objects to be published in the web.
    '''
    
    @cherrypy.expose
    def index(self):
        "This is the default object view." 
        return "Hello World!"


def _script():
       '''
       Publishes a HelloWorld object in the web.
       '''
       print('executing', sys.argv[0])
       print()
       cherrypy.config.update({'server.socket_port':8081})
       root = HelloWorld()
       cherrypy.quickstart(root)
      

        
if __name__=='__main__':
   _script()

