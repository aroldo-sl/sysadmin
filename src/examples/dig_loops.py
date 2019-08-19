#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file  dig_loops.py
# @date  2013-05-01
# @author Aroldo Souza-Leite
"""
Some loops in Python.
"""
################ <module boilerplate>  ######
from __future__ import print_function
####
echo = print

echo("hello")

#
post = ["Mary" , "Betty", "Kate", "Lucy"]
count = len

fmtstr = "Die Person {pe} kommt im Platz {pl} der Liste"


# for(i=0;i<count(post);i++){
# ...............
#} 
i = 0
while i<count(post):
    text = fmtstr.format(pe=post[i], pl=i+1)
    echo(text)
    i = i+1 # i++

echo()
echo("sortierte Liste wird ausgegeben:")
post.sort()
i = 0
while i<count(post):
    text = fmtstr.format(pe=post[i], pl=i+1)
    echo(text)
    i = i+1 # i++

echo()

# echo i++
echo(i)
i = i+1
#
# echo ++i
i = i+1
echo(i)    

# while (!$i)




