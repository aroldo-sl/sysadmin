#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  hooks00.py
# @date  2012-07-09
# @author Aroldo Souza-Leite
'''
A collection of test mercurial hooks.

This file is not necessarily under
version control.
'''
# singular imports from __future__
from __future__ import print_function
#
import os
import sys
from datetime import datetime
import random
import string


def info(ui,
         repo,
         node,
         hooktype, 
         **kw):
       '''
       This is a general introspection hook.

       Used for learning Mercurial's pretxnchangegroup.
       Adapted from 
       http://stackoverflow.com/questions/7675917/

       This hook module is being developed in 
       mxen-dev:/repos/sandbox00.
       '''
       msg ='''
{dashes}
{stamp}
now = {now}
hook type = {hooktype}
{dashes}'''
       msg +='''
<introspection>
repo type = {type_repo}
node = {node}'''
       msg +='''
node type = {type_node}
repo[node] = {repo_node}
repo[node] hex = {repo_node_hex}
repo[node] ver = {repo_node_rev}
repo[node] type = {type_repo_node}
repo['tip'] = {repo_tip}
repo['tip'] hex = {repo_tip_hex}
repo['tip'] rev = {repo_tip_rev}
repo['tip'] type = {type_repo_tip}
incoming range = {incoming_range}
</introspection>
{dashes}
'''
       dashes = '-' *30
       now = datetime.now()
       stamp = ''.join(random.sample(string.letters,5))
       # # <introspection>
       node = node
       type_node = type(node)
       type_repo = type(repo)
       repo_node = repo[node]
       repo_node_hex = repo[node].hex()
       repo_node_rev = repo[node].rev()
       type_repo_node = type(repo[node])
       repo_tip = repo['tip']
       type_repo_tip = type(repo['tip'])
       repo_tip_hex = repo['tip'].hex()
       repo_tip_rev = repo['tip'].rev()
       incoming_range = range(repo_node_rev, repo_tip_rev + 1)
       # # </introspection>
       msg = msg.format(dashes = dashes,
                        stamp = stamp,
                        now = now,
                        hooktype = hooktype,
       #                  # <introspection>
                         repo = repo,
                         type_repo =  type_repo,
                         node = node,
                        type_node = type_node,
                        repo_node = repo_node,
                        repo_node_hex = repo_node_hex,
                        repo_node_rev = repo_node_rev,
                        type_repo_node = type_repo_node,
                        repo_tip = repo_tip,
                        repo_tip_hex = repo_tip_hex,
                        repo_tip_rev = repo_tip_rev,
                        type_repo_tip = type_repo_tip,
                        incoming_range = incoming_range,
                        # </introspection>
                        )
       for rev in incoming_range:
           description = repo[rev].description()
           user = repo[rev].user()
           branch = repo[rev].branch()
           msg += '\n' + user + ' pushing \t' + branch
       msg +='\n'
       with open("hook.report", 'a') as hook_report:
           print(msg,file =hook_report )
       ui.write(str((node, repo[node])) + msg)

# found in http://stackoverflow.com/questions/7675917/automating-review-requests-with-reviewboard-and-mercurial-using-python-hooks/8615156#8615156

def checkAllCommitMessage(ui, repo, node, **kwargs):
    """    
    Checks all inbound changeset messages from a push for adherence to the commit message rules.
    """

    # for each change being submitted
    # get all the details, and call the trigger
    fail = False

    for rev in xrange(repo[node].rev(), len(repo)):
        # get context (change)
        ctx = repo[rev]

        # user who commited the change (NOT necessarily the one who is doing push)
        user = ctx.user()

        # do the hook stuff here...
        # set fail to True if something goes wrong

    return fail


# found in http://mercurial.selenic.com/wiki/HookExamples

# from mercurial.node import bin, nullid
# from mercurial import util

# def hook(ui, repo, node, **kwargs):
#     n = bin(node)
#     start = repo.changelog.rev(n)
#     end = len(repo.changelog)
#     failed = False
#     for rev in xrange(start, end):
#         n = repo.changelog.node(rev)
#         ctx = repo[n]
#         p = ctx.parents()
#         if ctx.branch()  == 'stable' and len(p) == 1:
#             if p[0].branch() != 'stable':
#                 # commit that creates the branch, allowed
#                 continue
#             ui.warn(' - changeset %s on stable branch and is not a merge !\n'
#                   % (ctx))
#             failed = True
#     if failed:
#         ui.warn('* Please strip the offending changeset(s)\n'
#                 '* and re-do them, if needed, on another branch!\n')
#         return True


