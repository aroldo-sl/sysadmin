#!python
# -*- coding:cp1252 -*-
'''
Instead of a DOS batch script.

Replaces 'make.bat' html from the
original Sphinx buildout recipe.
'''
from __future__ import print_function
import os
import sys
import subprocess
import webbrowser
import argparse

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
slog = _basic_logger(name="lib-docs")
############################## </module boilerplate> ########################################

def parse_arguments():
    '''
    Parses the command line arguments.

    Joins the  '--docs-interpreter' list to a file system
    path.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
           "--fire-up",
           dest = "fire_up",
           #metavar = "FIRE_UP",
           default = 'true',
           choices = ('true', 'false'),
           #action = "store_true",
           help=\
            "Open the browser on index.html (default: true)")
    parser.add_argument(
           "--buildout-directory",
           dest = "buildout_directory",
           #metavar = "BUILDOUT_DIRECTORY",
           default = None,
           action = "store",
           help=\
            "The root buildout directory of this project.")
    parser.add_argument(
           "--docs-interpreter",
           dest = "docs_interpreter",
           #metavar = "DOCS_INTERPRETER",
           nargs = '+',
           help=\
            "The Python (blank separated) path to the interpreter to call Sphinx."
           )
    args = parser.parse_args()
    args.fire_up = args.fire_up.lower()
    if args.buildout_directory is None:
        args.buildout_root_dir = os.getcwd()
    fire_up_bool = dict(true=True, false=False)
    args.fire_up = fire_up_bool[args.fire_up]
    docs_interpreter_list  = args.docs_interpreter
    docs_interpreter = os.path.join(*docs_interpreter_list)
    args.docs_interpreter = docs_interpreter
    return args

# def set_sphinx_options():
#     '''
#     Returns a dict with sphinx-build parameters.
#     '''
#     this_file  = os.path.abspath(sys.argv[0])
#     buildout_workdir = _buildout_workdir
#     bin_dir = os.path.join(buildout_workdir, 'bin')
#     parts_dir = os.path.join(buildout_workdir, 'parts')
#     docs_dir = os.path.join(parts_dir, 'docs')
#     html_dir = os.path.join(docs_dir, 'html')
#     source_dir = os.path.join(buildout_workdir, 'src', 'docs')
#     SPHINXBUILD    = os.path.join(bin_dir, 'sphinx-build')
#     # <Windows>
#     # remove this trick (because easy_install sphinx in Windows like this):
#     if os.name == 'nt':
#         SPHINXBUILD    = os.path.join(bin_dir, 'sphinx-build-script.py')
#     # </Windows>
#     BUILDDIR       = docs_dir
#     doctrees_dir   = os.path.join(BUILDDIR, 'doctrees')
#     html_dir       = os.path.join(BUILDDIR, 'html')
#     SPHINXOPTS     = '-E'
#     ALLSPHINXOPTS  = " ".join((   "-d",
#                                   doctrees_dir,
#                                   SPHINXOPTS,
#                                   source_dir,
#                               ))

#     return dict(SPHINXBUILD=SPHINXBUILD, BUILDDIR=BUILDDIR,
#                 SPHINXOPTS=SPHINXOPTS, ALLSPHINXOPTS=ALLSPHINXOPTS, html_dir=html_dir)

def make_sphinx_build_cmd(extra_sphinx_build_options = ("-E",)):
    """
    Makes the Sphinx build command using basically
    the default Sphinx build parameters.

    There is a quirk in this code trying to deal with the
    way "easy_install" installs Sphinx in Windows.
    Please see the code comments.

    @parameter extra_sphinx_build_options = ("-E",)
     The Sphinx build option "-E" deactivates the
     Sphinx build cache.
    """
    args = parse_arguments()
    SPHINXBUILD = 'sphinx-build'
    # <Windows>
    # This trick is necessary because of how "easy_install" 
    # installs sphinx in Windows:
    if os.name == 'nt':
        SPHINXBUILD    = 'sphinx-build-script.py'
    # </Windows>
    SPHINXBUILD = os.path.join(args.buildout_directory, 'bin', SPHINXBUILD)
    source_directory = os.path.join(args.buildout_directory,'src', 'docs')
    target_directory = os.path.join(args.buildout_directory,'parts','docs','html')
    sphinx_build_cmd = (args.docs_interpreter, SPHINXBUILD) +\
                       extra_sphinx_build_options +\
                       (source_directory, target_directory)
    sphinx_build_cmd = list(sphinx_build_cmd)
    slog.info('sphinx build command: {sphinx_build_cmd}'.format(sphinx_build_cmd = sphinx_build_cmd))
                       
    return sphinx_build_cmd

def call_sphinx_cmd(extra_sphinx_build_options = ("-E",)):
    '''
    Calls the Sphinx command in a subprocess.
    '''
    sphinx_build_cmd = make_sphinx_build_cmd(
                  extra_sphinx_build_options = extra_sphinx_build_options)
    return_code = subprocess.call(sphinx_build_cmd, shell=False)
    return return_code

def fire_up():
    '''
    Calls the web browser on index.html.
    '''
    args = parse_arguments()
    index_html = os.path.join(args.buildout_directory,
                                 'parts', 
                                 'docs',
                                 'html', 
                                 'index.html')
    slog.info("html index:" + index_html)
    webbrowser.open(index_html)

def _script():
    '''
    To be called if this is the main module.
    '''
    call_sphinx_cmd()
    args = parse_arguments()
    if args.fire_up:
        fire_up()


if __name__== '__main__':
    _script()

