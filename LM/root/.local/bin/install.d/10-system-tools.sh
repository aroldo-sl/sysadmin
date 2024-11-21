#!/usr/bin/env bash
packages=(
git
git-extras
gnome-system-tools
gparted
openssh-client
openssh-server
podman
rdiff-backup
restic
skopeo
stow
tree
uidmap
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
