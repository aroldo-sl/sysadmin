#!/usr/bin/env bash
# @file: install-00.sh
# @date: 2021-05-13
# @modified: 2021-05-13
# @comment: Calls install_00.py 
this_script=$(realpath $0)
workdir=$(dirname $this_script)
cd $workdir
echo "work directory:$workdir"
logfile="${this_script}.log"
echo "BEGIN of $this_script"
echo $(date +"%FT%H-%M-%S") |tee -a $logfile
cmd="./install.py $@ |tee -a $logfile"
if test $1 != "0"
   then
       # eval $cmd
   else
       echo $cmd
       echo "dry run"
fi
echo "END of $this_script"
echo "logfile: $(realpath $logfile)"
