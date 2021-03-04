#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  acl.py
# @date  2012-09-18
# @author Aroldo Souza-Leite
'''
Digging the Zope access control in Grok.
'''
# singular imports from __future__
from __future__ import print_function
#
import os
import sys
# a very simple pre-cofingured logger
from lb.slog import get_slog
slog = get_slog()
import grok

class UpdateSoftness(grok.Permission):
    '''
    Permission to update the softness attribute.
    '''
    grok.name('mycave.stones.update_softness')


class UpdateHardness(grok.Permission):
    '''
    Permission to update the hardness attribute.
    '''
    grok.name('mycave.stones.update_hardness')


class HardRole(grok.Role):
    '''
    A hardened role MyCave.
    '''
    grok.name('mycave.Hard')
    grok.title('Hard Role')
    grok.permissions('mycave.stones.update_hardness')


class SoftRole(grok.Role):
    '''
    A softened role in MyCave.
    '''
    grok.name('mycave.Soft')
    grok.title('Soft Role')
    grok.permissions('mycave.stones.update_softness')

