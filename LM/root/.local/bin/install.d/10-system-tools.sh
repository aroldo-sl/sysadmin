#!/usr/bin/env bash
packages=(
gnome-system-tools
gparted
restic
git
uidmap
podman
skopeo
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
