#!/usr/bin/env bash
# from https://linuxhandbook.com/rootless-docker/

timestamp=$(date +'%FT%Y-%m-%d-%S-%N')
logfile=${0//.sh/}-${timestamp}.log

purge_list=(
    docker
    docker.io
    docker-ce
    docker-engine
    docker-ce-cli
    containderd
    containerd.io
    containerd.io
    runc
    )

install_list=(
    newuidmap
    newguidmap
    dbus-user-session
    fuse-overlayfs
    docker
    docker-ce
    docker-engine
    docker-ce-cli
    containderd
    runc
    )

aptitude -y update

for package in ${purge_list[@]}
               do
                   echo "purging $package"
                   aptitude -y purge $package |tee -a $logfile
                   echo
               done

for package in ${install_list[@]}
  do
    echo "installing $package"
    aptitude -y install $package |tee -a $logfile
    echo
  done


systemctl disable --now docker.service docker.socket |tee -a $logfile

curl -fsSL https://get.docker.com -o get-docker.sh
chown aroldo:aroldo get-docker.sh
chmod 755 get-docker.sh
ls -l "get-docker.sh"
# ./get-docker.sh |tee $logfile
