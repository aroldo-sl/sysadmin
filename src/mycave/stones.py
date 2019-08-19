#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  stones.py
# @date  2012-08-29
# @author Aroldo Souza-Leite
'''
Examples of  IContentType usage.

The egg zope.app.content has to be
included in the 'mitcon.cfg' buildout
configuration file.
'''
from __future__ import print_function
#
import grok
import time
from zope.app.content import IContentType
# from zope.interface import implements
from lb.slog import get_slog
_logger = get_slog()

class IStone(IContentType):
    '''
    A stone.
    '''

class ISoftStone(IStone):
    '''
    A soft stone.
    '''

class IMediumStone(IStone):
    '''
    A medium hardness/softness stone.
    '''

class IHardStone(IStone):
    '''
    A hard stone.
    '''

class Stone(grok.Model):
    '''
    A stone.
    '''
    grok.implements(IStone)

    def __init__(self,name="stone-" + str(time.time())):
        self.name = name

class SoftStone(Stone):
    '''
    A soft stone.
    '''
    grok.implements(ISoftStone)
    grok.require('mycave.stones.update_softness')

    def __init__(self,name="softstone-" + str(time.time()), softness = 1, density = 0):
        super(SoftStone,self).__init__(name=name)
        self.softness = softness
        self.density = density

class MediumStone(Stone):
    '''
    A medium hardness/softness stone.
    '''
    grok.implements(IMediumStone)

    def __init__(self,name="mediumstone-" + str(time.time()), density = 0):
        super(MediumStone,self).__init__(name=name)
        self.density = density 

class HardStone(Stone):
    '''
    A hard stone.
    '''
    grok.implements(IHardStone)
    grok.require('mycave.stones.update_hardness')

    def __init__(self,name="hardstone-" + str(time.time()), hardness = 1, density = 0):
        super(HardStone,self).__init__(name=name)
        self.hardness = hardness
        self.density = density

# Views

class  IStoneView(grok.interfaces.IGrokView):
    '''
    Classes that implement this are to be declared untrusted.
    '''


class StoneView(grok.View):
    '''
    To be declared untrusted in ZCML.
    '''
    grok.implements(IStoneView)
    grok.context(IStone)
    grok.template('index')
    grok.name('index')

class SoftStoneView(StoneView):
    '''
    A soft stone view.
    '''
    grok.context(ISoftStone)
    grok.name('sindex')
    grok.template('soft_index')

    def update(self, 
               softness = None, 
               density = None):
        '''
        Sets the softness and the density.
        '''
        if softness is not None:
            self.context.softness = softness
        if density is not None:
            self.context.density = density
        self.softness = self.context.softness
        self.density = self.context.density

class MediumStoneView(StoneView):
    '''
    A medium stone view.
    '''
    grok.context(IMediumStone)
    grok.name('mindex')
    grok.template('medium_index')

    def update(self, 
               density = None):
        '''
        Sets the density.
        '''
        if density is not None:
            self.context.density = density
        self.density = self.context.density

class HardStoneView(StoneView):
    '''
    A hard stone view.
    '''
    grok.context(IHardStone)
    grok.name('hindex')
    grok.template('hard_index')

    def update(self,
               hardness = None, 
               density = None):
        '''
        Sets the hardness and the density.
        '''
        if hardness is not None:
            self.context.hardness = hardness
        if density is not None:
            self.context.density = density
        self.hardness = self.context.hardness
        self.density = self.context.density


