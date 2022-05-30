#!/usr/bin/env bash
# @file: install-00.sh
# @date: 2021-05-13
# @modified: 2021-05-13
# @comment: Calls install_00.py 
this_script=$(realpath $0)
workdir=$(dirname $this_script)
cd $workdir
echo "work directory:$workdir)"
logfile="$workdir/install.log"
echo "BEGIN of $this_script"
echo $(date +"%FT%H-%M-%S") |tee -a $logfile
time ./install_00.py |tee -a $logfile
echo "END of $this_script"
echo "logfile: $(realpath $logfile)"
