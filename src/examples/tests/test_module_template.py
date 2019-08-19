#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  test_2_module_template.py
# @date  2012-07-31
# @author Aroldo Souza-Leite
'''
pytest tests for module_template.py.

To write a test module for an arbitrary
Python module, copy this module and overwrite the
text block '# specific imports...'.
'''
from __future__ import print_function

# general imports for all test modules
import pytest

########### specific imports for this test module #################
from ..module_template import (the_truth, 
                              the_untruth,
                              jump_off,
                              )
import os
from datetime import datetime
import tempfile
import shelve
###################################################################

def make_timestamp(fmt = '{year}-{month}-{day}-{hour}' +\
                         '{minute}-{second}-{microsecond}',
                   now = None):
    '''
    Returns a timestamp in a comfortable format ('fmt').

    Makes a dictionary out of the attributes (time units)
    of a datetime.datetime instance ('now').
    '''
    if now is None:
        now = datetime.now()
    time_units = ('year', 'month', 'day', 'hour', 
                  'minute', 'second', 'microsecond')
    time_dict = {time_unit:getattr(now,time_unit) for time_unit in time_units}
    timestamp = fmt.format(**time_dict)
    return timestamp

def setup_module(module):
    '''
    Creates a temporary persistent dictionary-like object.

    Uses the standard Python tmpfile module to find a temporary
    directory accessible without root rights (in Linux: /tmp/...).
    '''
    global tmpdir, shelf
    tmpdir = tempfile.mkdtemp(prefix='pytest_' + make_timestamp())
    shelf_name = os.path.join(tmpdir, 'shelf')
    shelf = shelve.open(shelf_name, writeback = True)
    shelf['greeting'] = 'hello'

def teardown_module(module):
    '''
    Closes the persistent dictionary-like object.
    '''
    global tmpdir, shelf
    shelf.close()
    ## uncomment the lines below if you don't need the persistent
    ## dictionary after the test is over.
    # import shutil
    # shutil.rmtree(tmpdir)
    
def test_shelf():
    '''
    Tests the global shelf.

    Makes sure that the shelf object
    is available for all the test functions
    in this test module.
    '''
    assert 'greeting' in shelf
    shelf['comment'] = 'good'

def test_jump_off():
    '''
    Tests if jump_off really stops Python.
    '''
    with pytest.raises(SystemExit) as r:
        jump_off()
        # how to include these lines in the test report?
        print("In production, this will raise the follwing exception:")
        print(r.getrepr())

def test_truth_1():
    '''
    Should fail.
    '''
    assert the_truth() is False

def test_truth_2():
    '''
    Should pass.
    '''
    assert the_truth() is True

def test_untruth_2():
    '''
    Should fail.
    '''
    assert the_untruth() is True

def test_untruth_1():
    '''
    Should pass.
    '''
    assert the_untruth() is False
