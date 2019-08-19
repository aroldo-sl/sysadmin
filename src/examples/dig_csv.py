#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  dig_csv.py
# @date  2012-04-13
# @author Aroldo Souza-Leite
'''
short description

long description
long description
'''

from __future__ import print_function
import os
import sys
import csv

import time
from lb.slog import get_slog
_logger = get_slog()

def read_csv_data(csv_path = ('data', 'PommesBude.csv')):
    '''
    Reads the data into a dictionary.
    '''
    csv_path = os.path.join(*csv_path)
    _logger.info(str(csv_path))
    if not os.path.isfile(csv_path):
        raise IOError("file {csv_path} doesn't exist".format(csv_path = csv_path))
    csv_file = open(csv_path)
    dreader = csv.DictReader(csv_file)
    rows = list(dreader)
    csv_file.close()
    result =  {'fieldnames':dreader.fieldnames,"rows":rows}
    return result

def test_quality():
    '''
    Tests 'Quality' in field names.
    '''
    result = read_csv_data()
    fieldnames = result['fieldnames']
    rows = result['rows']
    assert "Quality" in fieldnames


def test_row_0():
    '''
    Tests if row[0] is a dictionary.

    Looks up the value of "Quality".    
    '''
    result = read_csv_data()
    fieldnames = result['fieldnames']
    rows = result['rows']
    assert rows[0]["Quality"] == "mediocre"


def test_last_row():
    '''
    Tests if row[-1] is a dictionary.

    Looks up the value of "Name".    
    '''
    result = read_csv_data()
    fieldnames = result['fieldnames']
    rows = result['rows']
    assert rows[-1]["Name"] == "ketchup"
      


def _script():
       '''
       Intended to be invoked only if this is the __main__ module.
       '''
       _logger.info('executing ' + __file__ + '._script')
       result = read_csv_data()
       _logger.info(str(result))
       
if __name__=='__main__':
   _script()

