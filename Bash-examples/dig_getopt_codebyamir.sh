#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# @file  dig_getopt_codebyamir.sh
# @date  20 Mai 2019
# @author Aroldo Souza-Leite
# @from https://www.codebyamir.com/blog/parse-command-line-arguments-using-getopt

# Parse command-line options

# Option strings
SHORT=vf:
LONG=verbose,file:

# read the options
OPTS=$(getopt --options $SHORT --long $LONG --name "$0" -- "$@")

if [ $? != 0 ] ; then echo "Failed to parse options...exiting." >&2 ; exit 1 ; fi

# eval this seems to be necessary because $OPTS returns quoted values?
eval set -- "$OPTS"

# set initial values
VERBOSE=false

# extract options and their arguments into variables.
while true ; do
  case "$1" in
    -v | --verbose )
      VERBOSE=true
      shift
      ;;
    -f | --file )
      FILE="$2"
      shift 2
      ;;
    -- )
      shift
      break
      ;;
    *)
      echo "Internal error!"
      exit 1
      ;;
  esac
done

# Print the variables
echo "VERBOSE = $VERBOSE"
echo "FILE = $FILE"

