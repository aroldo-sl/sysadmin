#!/usr/bin/env bash
packages=(
        # arp-scan
        # default-jdk
        # ffmpeg
        # fsarchiver
        guile-3.0    # Gnu Scheme
        guile-3.0-dev
        # geany
        ## gimp
        # git
        # git-extras
        # gnome-system-tools
        # gparted
        # librsvg2-bin
        # members                   # bluetooth
        # most
        # nmap
        # openssh-client
        # openssh-server
        # pandoc
        # podman
        # qtcreator
        # rdiff-backup
        # restic
        scheme9
        # sshfs
        # skopeo
        # sshfs
        # stow
        # terminator
        # tree
        # uidmap
        # wl-clipboard
        # xclip
        # xsel
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
