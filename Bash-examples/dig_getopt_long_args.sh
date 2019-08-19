#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# @file  dig_getopt_long_args.sh
# @date  20 Mai 2019
# @author Aroldo Souza-Leite

## original first line:
#!/bin/bash -e

ARGUMENT_LIST=(
    "arg-one"
    "arg-two"
    "arg-three"
)


# read arguments
opts=$(getopt \
    --longoptions "$(printf "%s:," "${ARGUMENT_LIST[@]}")" \
    --name "$(basename "$0")" \
    --options "" \
    -- "$@"
)

eval set -- $opts

while [[ $# -gt 0 ]]; do
    case "$1" in
        --arg-one)
            argOne=$2
            shift 2
            ;;

        --arg-two)
            argTwo=$2
            shift 2
            ;;

        --arg-three)
            argThree=$2
            shift 2
            ;;

        *)
            break
            ;;
    esac
done

echo "--arg-one=$argOne"
echo "--arg-two=$argTwo"
echo "--arg-three=$argThree"
