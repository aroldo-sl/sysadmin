#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  paster-serve-debug.py
# @date  2012-10-17
# @author Aroldo Souza-Leite
'''
Runs the Grok framework in default manner.
'''
############################## <module boilerplate> ########################################
from __future__ import print_function
import os
import  sys
import subprocess
def _basic_logger(name = None, 
                  level = None, # default: logging.DEBUG
                  stream = sys.stderr,
                 ):
    '''
    A logger from a 'logging' basic configuration.
    
    A simple but more flexible logger can 
    be imported from the package lb.slog.

    @return slog : a basic configured logger.
    '''
    # default name
    if name is None:
        import time
        name = sys.argv[0]
        name = os.path.splitext(name)[0]
        name = name + '.' + str(time.time())
    import logging
    if level is None:
        level = logging.DEBUG
    logging.basicConfig()
    slog = logging.getLogger(name)
    from logging import StreamHandler
    handler = StreamHandler(stream)
    slog.setLevel(level)
    return slog
slog = _basic_logger()
############################## </module boilerplate> ########################################

import argparse
def _parse_cli_arguments():
    '''
    Parses the command line arguments.

    @return args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--paster-cmd-location', 
                        help = 'The (blank-separated) path to the paster cmd.',
                        metavar = 'P',
                        nargs = '+',
                        dest = 'paster',
                        )
    parser.add_argument('-i',
                        '--inifile-location',
                        help = 'The (blank-separated) path to the ini file.',
                        metavar = 'I',
                        nargs = '+',
                        dest = 'inifile',
                       )
    args = parser.parse_args()
    return args


def check_cli_arguments():
    '''
    Checks if argparse is working.
    '''
    args = _parse_cli_arguments()
    paster2 = os.path.join(*args.paster)
    paster2 = os.path.abspath(paster2)
    inifile2 = os.path.join(*args.inifile)
    inifile2 = os.path.join(*inifile2)
    janein = {True:'ja', False:'nein'}
    msg = '''
Parsed cli argumengs:
paster->{paster}
paster2> {paster2} (exists? {paster_exists})
inifile->{inifile}
inifile2->{inifile2} (exists? {inifile_exists})
'''
    msg = msg.format(paster = args.paster,
                     paster2 = paster2,
                     paster_exists = janein[os.path.exists(paster2)],
                     inifile = args.inifile,
                     inifile_exists = janein[os.path.exists(inifile2)],
                     inifile2 = inifile2,
                     )
    slog.info(msg)


def build_command():
    '''
    Builds the command to be called.
    '''
    args = _parse_cli_arguments()
    paster = os.path.join(*args.paster)
    paster = os.path.abspath(paster)
    inifile = os.path.join(os.path.join(*args.inifile))
    inifile = os.path.abspath(inifile)
    cmd = ' '.join((paster, "serve", inifile))
    return cmd

def call_command():
    '''
    Calls the command built by build_command.
    '''
    cmd = build_command()
    slog.info("calling:" + cmd)
    subprocess.call(cmd, shell=True)
    return 0


def _script():
       '''
       Intended to be invoked if this module is called as a script.
       '''
       # check_cli_arguments()
       cmd = build_command()
       slog.info('command:' + cmd)
       call_command()

if __name__=='__main__':
   _script()

