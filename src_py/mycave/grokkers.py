#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  grokkers.py
# @date  2012-10-01
# @author Aroldo Souza-Leite
'''
Complementary grokkers for mycave.
'''
# singular imports from __future__
from __future__ import print_function
#
from lb.slog import get_slog
slog = get_slog()
import grok
import grokcore.security
import zope.publisher
import martian
from .stones import Stone, IStone, IHardStone, ISoftStone, IMediumStone

stone_interfaces = (IStone, IHardStone, ISoftStone, IMediumStone)


"""
class StoneSecurityGrokker(martian.ClassGrokker):
    '''
    Groks the Stone class (and subclasses).

    Pladgiarized from the View grokker example in
    http://pypi.python.org/pypi/grokcore.security

    This security grokker activates the security proxy using
    grokcore.security.util.get_attribute.
    '''
    martian.component(Stone)
    martian.directive(grok.require, name='permission')

    def execute(self, class_, config, permission, **kw):
        # select which interfaces from the Stones module are
        # implemented by the class being grokked.
        istones = (istone for istone in stone_interfaces if istone.implementedBy(class_))
        for istone in istones:
              for method_name in istone:
                  config.action(
                      discriminator=('protectName', class_, method_name),
                      # ATTENTION: the View grokker example mentioned in
                      # the docstring above uses protect_getattr
                      callable=grokcore.security.util.protect_getattr,
                      args=(class_, method_name, permission),
                      )
        return True

"""
