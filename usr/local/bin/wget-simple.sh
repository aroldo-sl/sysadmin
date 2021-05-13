!#/usr/bin/env bash
# @file: wget-simple.sh
# @date: 2021-05-08
# @modified: 2021-05-08
# @author: Aroldo Souza-Leite
# @comment: Copied from a very old script in sysadmin/usr.local.bin

PAGE=$1
wget --no-parent --no-host-directories -rk -t inf "$PAGE" 