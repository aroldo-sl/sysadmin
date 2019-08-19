#!python
# -*- coding: cp1252 -*-
#
# @file  m03_cherry_form.py
# @date  2012-04-16
# @author Aroldo Souza-Leite
'''
CherryPy publishes an object with many views.

Includes a HTML form.
'''
from __future__ import print_function
#
import sys
import cherrypy
from datetime import datetime


# example adapted from 
# http://sschwarzer.com/de/talks/cherrypy
class HelloForm(object):
    '''
    Exposes a form with itself as the action.

    The form calls action methods explicitly
    depending on the GET parameter values.

    Using a static method:
  
    >>> cl = HelloForm
    >>> cl.template #doctest: +ELLIPSIS
    <function template at 0x...>
    >>> cl.template(body_content='currywurst')
    '<html><head><title>CherryPy demonstration</title></head>\n                <body>currywurst</body></html>'
    '''

    @staticmethod   
    def template(body_content):
        '''
        This is a static method.

        Call HelloForm.template (without a class object).

        >>> html = HelloForm.template('currywurst')
        >>> 'currywurst' in html
        True
        >>> 'pommes' in html
        False
        '''
        
        t = """<html><head><title>CherryPy demonstration</title></head>
                <body>{body_content}</body></html>"""
        return t.format(body_content=body_content)
        
    @cherrypy.expose   
    def index(self):
        '''
        Publishes a string with a dynamic date object representation.
        '''
        return 'Hello from CherryPy at {now}'.format(now=datetime.now())

    @cherrypy.expose
    def form(self, first_name=None, last_name=None, submit_names=None):
        '''

        >>> root = HelloForm() # Erstellung eines Objekts der Klasse HelloForm
        >>> html = root.form(first_name='Willi', last_name='Klug', submit_names = 'yes')
        >>> 'Willi' in html
        True
        >>> 'Klug' in html
        True
        >>> 'Ja, so isses' in html
        False
        '''
        
        if first_name and last_name and submit_names:
               return self.confirmation(first_name=first_name, last_name=last_name)
        first_name, last_name = (last_name, first_name)
        form_body = """
        <form method="POST">
        Vorname:  <input type="text" name="first_name" value="{first_name}"/><br />
        Nachname: <input type="text" name="last_name" value="{last_name}"/><br />
        <input type="submit" name="submit_names" value="Ja, so isses" />
        </form>
        """.format(first_name=first_name, last_name=last_name) + str(datetime.now())
        return self.template(form_body)

    def confirmation(self, first_name=None, last_name=None):
        if any((first_name is None, last_name is None)):
               result = "Nothing to confirm"
               return result
        confirmation_body = "Hallo, {0} {1}!".format(first_name, last_name)
        result = self.template(confirmation_body)
        return result 

def _script():
    '''
    Intended to be invoked if this module is called as a script.
    '''
    print('executing', sys.argv[0]) 
    root = HelloForm()
    cherrypy.config.update({'server.socket_port':8081})
    cherrypy.quickstart(root)

if __name__=='__main__':
   _script()

