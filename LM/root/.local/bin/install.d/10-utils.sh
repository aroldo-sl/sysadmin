#!/usr/bin/env bash
packages=(
#vimtutor # not found
#xapp #dependency error
ffmpeg
geany
git
git-extras
gnome-system-tools
gparted
librsvg2-bin
members
most
openssh-client
openssh-server
pandoc
podman
qtcreator
rdiff-backup
restic
skopeo
stow
terminator
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