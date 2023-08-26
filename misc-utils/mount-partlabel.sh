#!/usr/bin/env bash
# filename:mount-partlabel.sh
error_handle() {
    error_code=$?
    caller_=$(realpath -P $(caller))
    printf "ERROR in $caller_\n"
    printf "line:${BASH_LINENO[0]}\n"
    printf "Bash command \'$BASH_COMMAND\'\n"
    printf "error_code:$error_code\n"
     exit $error_code
}
trap error_handle ERR 
partlabel=$1
device=/dev/disk/by-partlabel/$partlabel
ls $device 

# mount_dir=/mnt/$partlabel
# if [[ ! -d $mount_dir ]]
# then
#      mkdir $mount_dir
#      printf "created $mount_dir\n"
# else
#      printf "$mount_dir exists already\n"
# fi
# printf  "mount $device $mount_dir\n"
printf "End of $(realpath $0)\n"
