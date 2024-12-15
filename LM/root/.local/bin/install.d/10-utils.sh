#!/usr/bin/env bash
packages=(
        #vimtutor # not found
        #xapp #dependency error
        arp-scan
        default-jdk
        ffmpeg
        geany
        git
        git-extras
        gnome-system-tools
        gparted
        librsvg2-bin
        members                   # bluetooth
        most
        nmap
        openssh-client
        openssh-server
        pandoc
        podman
        qtcreator
        rdiff-backup
        restic
        sshfs
        skopeo
        sshfs
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
