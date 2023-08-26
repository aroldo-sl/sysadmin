#!/usr/bin/env bash
# filename:mount-partlabel.sh
# set -u # forbids the usage of unset variables
# set -e # exits when an error occurs.
script=$(realpath -P $0)
error_log=$(mktemp)
error_handle() {
    error_code=$?
    printf "ERROR in $script:${BASH_LINENO[0]}\n"
    printf "Bash command:$BASH_COMMAND\n"
    cat $error_log
    printf "error code:$error_code\n"
    error_log=$(mktemp)
}
trap error_handle ERR

exit_handle() {
    error_code=$?
    printf "ERROR (EXIT) in $script:${BASH_LINENO[0]}\n"
    printf "Bash command:$BASH_COMMAND\n"
    cat $error_log
    printf "error code:$error_code\n"
    exit $error_code
}
trap exit_handle EXIT


partlabel=$1
device=/dev/disk/by-partlabel/$partlabel
ls $device 2>$error_log
mount_dir=/mnt/$partlabel
if [[ ! -d $mount_dir ]]
then
      mkdir $mount_dir
      printf "created $mount_dir\n"
else
      printf "$mount_dir already exists\n"
fi
if [[ ! $(mountpoint $mount_dir) ]]
then
       echo "$mount_dir is already a mount point"
else
       echo "mounting $device on $mount_dir"
       mount $device $mount_dir
fi
echo "final mount status: $(findmnt -M $mount_dir -n -o  TARGET,SOURCE)"
echo "End of $script"

