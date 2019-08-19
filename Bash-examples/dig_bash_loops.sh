#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# @file  dig_bash_loops.sh
# @date  01 Mai 2019
# @author Aroldo Souza-Leite
#

# building an array of input parameters (including the script itself)
all=( $0 $@ )
END=$#
# NOTA BENE: END and not $END (!!!!!)
for ((i=0;i<=END;i++)); do
    echo "$i -> ${all[$i]}"
done




