#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# @file  dig_getopt_00.sh
# @date  03 Jun 2019
# @author Aroldo Souza-Leite
#



arr=(a b c "D and E")
echo "Array 'arr' with "${#arr[@]}" entries:"
for((i=0;i<${#arr[@]};i++))
do
    echo "arr[$i]=${arr[$i]}"
done

echo
echo "the original script parameters:"
echo $@

set -- "${arr[@]}"

echo
echo "the script parameters set internally in the script:"
echo "there are now $# set parameters:"
for((i=0;i<${#@};i++))
do
    echo "$i -> ${!i}"
done



