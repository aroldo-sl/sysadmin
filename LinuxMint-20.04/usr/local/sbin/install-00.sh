#!/usr/bin/env bash
# @file: install-00.sh
# @date: 2021-05-13
# @modified: 2021-05-13
# @comment: Calls install_00.py 
logfile="install.log"
echo $("BEGIN of $0")
echo $(date +"%FT%H-%M-%S") |tee -a $logfile
time ./install_00.py |tee -a $logfile
echo "END of $0"
echo "logfile: $(realpath $logfile)"
