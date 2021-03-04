#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  perseus-to-krebs.py
# @date  2013-03-17
# @author Aroldo Souza-Leite
"""
perseus-xml to bkrebs-xml

Uses etree.
"""
# @file perseus_to_bkrebs.py
################ <module boilerplate>  ######
from __future__ import print_function
import os
import sys
__module_name__ = 'perseus_to_bkrebs'
def _basic_logger(name = None, 
                  level = None, # default: logging.DEBUG
                  stream = sys.stderr,
                 ):
    """
    A logger from a 'logging' basic configuration.
    
    A simple but more flexible logger can 
    be imported from the package mutils.loggingmx.

    @return slog : a basic configured logger.
    """
    # default name
    if name is None:
        import time
        name = __module_name__
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

################# </module boilerplate> #####

from xml.etree import ElementTree as etree

datadir = 'data'
perseus = (datadir, 'perseus')
bkrebs = (datadir, 'bkrebs')
docutils_xml = (datadir, 'docutils-xml')
_input_filename = 'thuc-01.009.xml'


def set_paths(input_filename= _input_filename,
              output_filename = None):
    """
    Sets input and output data paths.
    """
    if output_filename is None:
        output_filename = input_filename
    input_dirpath = os.path.join(*perseus)
    if not os.path.isdir(input_dirpath):
        raise IOError('input directory {directory} does not exist'.\
                       format(directory = input_filepath))
    output_dirpath = os.path.join(*bkrebs)
    if not os.path.isdir(output_dirpath):
        os.makedirs(output_dirpath)
    input_filepath = os.path.join(input_dirpath, input_filename)
    output_filepath = os.path.join(output_dirpath, output_filename)
    return input_filepath, output_filepath



def get_parent(tree=None, element=None):
    """
    Because child.find('..') doesn't work.
    """
        if tree is None:
            return None
        parent_map = ((c, p) for p in tree.getiterator() for c in p)
        (c,p) = (None,None)
        while not c is element:
            (c,p) = next(parent_map) 
        return p


def detatch(tree=None, element):
    """
    Removes an element from its parent.

    @return  parent
    """
    parent = get_parent(tree, element)
    if parent is not None:
        parent.remove(element)
    return parent

def TEI2bkrebsdoc(TEIdoc = None):
    """
    Transforms a perseus xml TEI xml tree into a bkrebs xml tree. 
    """
    # here we only need input_filepath
    if TEIdoc is None:
        input_filepath, output_filepath = set_paths(
                        input_filename= _input_filename)
        with open(input_filepath) as input_file:
            TEIdoc = etree.parse(input_file)
    bkrebsdoc = TEIdoc
    root = bkrebsdoc.getroot()
    book_marker =  root.find('.//*[@type="book"]')
    booknr = book_marker.get('n')
    chapter_marker = root.find('.//*[@unit="chapter"]')
    chapternr = chapter_marker.get('n')
    root.set('n', booknr + '.' + chapternr)
    detatch(chapter_marker)
    chapter_contents = root.find('text/body/div1/p')
    for element in chapter_contents:
        root.append(element)
    root.remove(root.find('text'))
    root.tag = 'chapter'
    return bkrebsdoc

def bkrebsdoc2docutilsdoc_iter(bkrebsdoc = None):
    """
    Transforms a bkrebsdoc tree in a docutils tree.
    """
    if bkrebsdoc is None:
        bkrebsdoc = TEI2bkrebsdoc()
    docutilsdoc = bkrebsdoc
    chapter = docutilsdoc.getroot()
    for element in chapter:
        parent = get_parent(element, bkrebsdoc)
        if parent is None:
            parent_tag = 'none'
        else:
            parent_tag = parent.tag
        yield {'element':element, 
               'tag':element.tag, 
               'unit':element.get('unit'),
               'parent_tag': parent_tag}
    
def write_out(tree = None, 
              filename = 'tmp.xml',
              dirpath  = ('data', 'tmp'),
              encoding = 'utf-8'):
    """
    Writes out an element tree to a file.

    If tree is None, bkrebsdoc2doctutilsdoc
    is calld with default parameters to 
    build the tree.
    """
    if tree is None:
        tree = bkrebsdoc2docutilsdoc()
    dirpath = os.path.join(*dirpath)
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
    filepath = os.path.join(dirpath,filename)
    tree.write(filepath, encoding = "utf-8", xml_declaration=True, method='xml')

def do_bkrebs(
       input_filename = _input_filename,
       output_filename = None
      ):
    """
    Does everything.
    """
    if output_filename is None:
        output_filename = input_filename
    input_filepath, output_filepath = set_paths(
                              input_filename = input_filename)
    slog.info("""
input file path  -> {infile}
output file path -> {outfile}""".format(
                 infile = input_filepath,
                 outfile = output_filepath))

    book = make_book(input_filename = input_filename)
    book = make_book(input_filename = input_filename)
    chapter = flatten_book(book = book)
    write_out(element = chapter,
              output_filepath = output_filepath,
              encoding = 'utf-8')
    return output_filepath

# %history -rf ipython-history.txt

def do_bkrebs_all():
    """
    Closure: uses 'perseus' and 'bkrebs'.
    """
    input_dirpath = os.path.join(*perseus)
    filenames = (os.path.basename(filepath)\
         for filepath in os.listdir(input_dirpath))
    for input_filename in filenames:
        do_bkrebs(input_filename = input_filename,
           output_filename = None)

def do_bkrebs_to_docutils():
    """
    Closure: uses 'bkrebs' and 'docutils_xml'.
    """
    input_dirpath = os.path.join(*bkrebs)
    output_dirpath = os.path.join(*docutils_xml)
    input_filenames = os.listdir(input_dirpath)
    for filename in input_filenames:
        input_filepath = os.path.join(input_dirpath, filename) 
        with open(input_filepath) as input_file:
            tree = etree.parse(input_file)
            chapter = tree.getroot()
        section = bkrebs_to_docutils_xml(chapter = chapter)
        output_filepath = os.path.join(output_dirpath, filename)
        write_out(element = section,
                  output_filepath = output_filepath,
                  encoding = 'utf-8')


def _script():
       """
       Intended to be invoked if this module is called as a script.
       """
       slog.info("starting '_script'")

       # do_bkrebs(
       # input_filename = 'thuc-02.053.xml',
       # output_filename = None
       # )

       # do_bkrebs_all()


if __name__=='__main__':
   _script()

