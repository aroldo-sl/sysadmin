#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# @file  dig_getopts.sh
# @date  01 Mai 2019
# @author Aroldo Souza-Leite
#

set -e
set -u
set -o pipefail

echo "try it like this: 'dig_getopts.sh -lha haha hihi hoho huhu'"
echo
n=$#
echo "number of parameters: $n"
for i in (( number=0; number <= $#; number++ )) 	 
do
    echo $i
done
    
    
    
    
    
echo "this the result of crude (non getopts) parsing before shifting:"
echo "0 -> $0"
echo "1 -> $1"
echo "2 -> $2"
echo "3 -> $3"
echo "4 -> $4"
echo "5 -> $5"

echo
echo "now the getopts parsing begins:"
dry_run="yes"

while getopts 'lhxa:' OPTION; do
  case "$OPTION" in
    l)
      echo "-l means linuxconfig"
      ;;

    h)
      echo "h stands for hopeless"
      ;;

    a)
      avalue="$OPTARG"
      echo "The value provided by -a is $avalue"
      ;;
    
    x)
	dry_run="no"
	echo "ACHTUNG: the dry-run flag is set to $dry_run"
	;;
    ?)
        echo "script usage: $(basename $0) [-l] [-h] [-a somevalue]" >&2
        exit 0
      ;;
  esac
done

if  [[ $dry_run == "yes" ]]
then
    
    echo "dry-run flag:$dry_run"
    exit 0
    echo "exited?"
fi
echo
shift "$(($OPTIND -1))"

    
echo "after shifting the following parameters were parsed:"
for value in $*
do
	     echo $value
done
