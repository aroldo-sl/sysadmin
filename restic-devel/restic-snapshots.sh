#!/bin/bash
## file restic-snapshots.sh

now="$(date +'%F-%H_%M_%S')"
logfile="restic-snapshots.log"
echo "repository:$(pwd)"  > "$logfile"
echo "datetime:$now" >> "$logfile"
echo "logging to $logfile"
restic snapshots -vr "$(pwd)" | tee -a "$logfile"
