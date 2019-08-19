#!/bin/bash
## @file restic-backup.sh

source="/"
repo="$(pwd)"

echo "restic backing up hp-lubuntu to repository $(realpath $repo)"

logfile="$(date +'%F-%H_%M_%S')-restic-backup.log"

time restic backup \
     --no-lock --no-cache \
     --tag Lubuntu-18.10-main \
     --exclude-file restic-backup-exclude.txt \
     -xvr $repo $source \
| tee $logfile

 

