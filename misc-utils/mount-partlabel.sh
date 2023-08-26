#!/usr/bin/env bash
# filename:mount-partlabel.sh
# set -u # forbids the usage of unset variables
# set -e # exits when an error occurs.
script=$(realpath -P $0)
error_log=$(mktemp)
error_handle() {
    error_code=$?
    printf "ERROR in $script:${BASH_LINENO[0]}\n"
    printf "$BASH_COMMAND\n"
    cat $error_log
    printf "error code:$error_code\n"
    exit $error_code
}
trap error_handle ERR
# trap error_handle EXIT
partlabel=$1
device=/dev/disk/by-partlabel/$partlabel
ls $device 2>$error_log
# mount_dir=/mnt/$partlabel
# if [[ ! -d $mount_dir ]]
# then
#       mkdir $mount_dir
#       printf "created $mount_dir\n"
# else
#       printf "$mount_dir exists already\n"
# fi
# printf  "mount $device $mount_dir\n"
echo "End of $script"

