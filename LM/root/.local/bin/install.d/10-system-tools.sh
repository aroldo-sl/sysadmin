#!/usr/bin/env bash
packages=(
gnome-system-tools
gparted
restic
git
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
