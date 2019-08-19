#!python
'''
Bootstraps a fresh work directory and and builds it out.

Uses the lb-buildout.cfg buildout configuration (as default).
Does not verifies command line arguments consistency.

Remark: the 'subprocess' calls tend to be unstable in
MS-Windows.
'''
from __future__ import print_function
printf = print
import os
import sys
import shutil
import subprocess
import logging
logging.basicConfig()
slog = logging.getLogger('lb')
slog.setLevel(logging.DEBUG)

def parse_arguments():
    '''
    Parses the command line arguments.


    The argparse configuration is somehow incomplete.
    @return args
    '''
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
           "--clean",
           dest = "clean",
           #metavar = "CLEAN",
           default = False,
           action = "store_true",
           help="cleans (wipes off) the parts under zc.buildout control")
    parser.add_argument(
           "--bootstrap",
           dest = "bootstrap",
           #metavar = "BOOTSTRP",
           default = False,
           action = "store_true",
           help="bootstraps the bin/buildout tool")
    parser.add_argument(
           "--buildout",
           dest = "buildout",
           # metavar = "BUILDOUT",
           default = False,
           action = "store_true",
           help="calls bin/buildout for lb-buildout.cfg")
    parser.add_argument(
           "--cfg", 
           nargs="*",
           dest = "cfg",
           default = None,
           help = """The path to the buildout configuratin file.
Separated by spaces."""
                   )
    args = parser.parse_args()
    if not args.cfg:
       args.cfg = ('lb-buildout.cfg',)
    return args


def test_parse_arguments():
    """
    Tets if the arguments were parsed ok.
    """
    args = parse_arguments()
    assert hasattr(args, 'clean')
    assert hasattr(args, 'bootstrap')
    assert hasattr(args, 'buildout')
    assert hasattr(args, 'cfg')
    

def clean(built  = (('bin',), 
                    ('parts',),
                    ('develop-eggs',),
                    ('.installed.cfg',),
                    ('extends-cache',)),
          restore = (('extends-cache',),)
                    ):
    '''
    Removes the 'built' files and directories.
    '''
    # os independent paths to the buildout elements:
    built = [os.path.join(*element) for element in built]
    def erase(filepath):
        if os.path.exists(filepath):
              if os.path.isdir(filepath):
                   shutil.rmtree(filepath)
              else:
                   os.remove(filepath)
    for filepath in built:
              slog.info("cleaning off " + filepath)
              erase(filepath)
    restore = [os.path.join(*element) for element in restore]
    for filepath in restore:
        os.mkdir(filepath)


def bootstrap(use_distribute=True):
    '''
    Bootstraps the buildout work directory.

    @process_output : the process output as str
    '''
    bootstrap_command = ['python', 'bootstrap.py']
    if use_distribute:
        bootstrap_command.append('-d')
    process_output = subprocess.check_output(
                            bootstrap_command,
                            # remark: I didn't understand the rationale 
                            # of shell=True or False in the 'subprocess'
                            # documentation.
                            shell = False)
    return process_output


def buildout(cfg = ( 'lb-buildout.cfg' ,)):
    '''
    Calls bin/buildout for the cfg configuration file.

    calls python processes with the 'subprocess' module.

    I didn't understand the rationale of 'shell=True' or
    'shell=False' in the Python 'subprocess' documentation.

    @par cfg (tuple)
         path to the buildout configuration file.
    '''
    cfg = os.path.join(*cfg)
    buildout_command = os.path.join('bin', 'buildout')
    cmd = [buildout_command, '-c', cfg]
    retcode = subprocess.call(cmd, 
                            # remark: I didn't understand the rationale 
                            # of shell=True or False in the 'subprocess'
                            # documentation.
                            shell=False)
    return retcode


def _script():
    '''
    Runs if the module is called as a script.
    '''
    slog.info("Running {script}.".format(script='lb-buildout.py'))
    args = parse_arguments()
    if args.clean:
         slog.info("cleaning off the buildout parts")
         clean()
    if args.bootstrap:
         slog.info("bootstraping")
         process_output = bootstrap()
         slog.info(process_output)
    if args.buildout:
         cfg = args.cfg
         slog.info("buildout configuration file path:{cfg}".format(cfg = cfg))
         slog.info("building out")
         rcode = buildout(cfg = cfg)
         slog.info("buildout return code: {rcode}".format(
                                                    rcode=rcode))


if __name__=='__main__':
    _script()


 
    








    








        

        
    
