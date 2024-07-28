#!/usr/bin/env bash
packages=(
#gnome-system-tools
#gparted
#restic
#rdiff-backup
#git
#uidmap
#podman
#skopeo
#openssh-client
#openssh-server
#git-extras
stow
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
