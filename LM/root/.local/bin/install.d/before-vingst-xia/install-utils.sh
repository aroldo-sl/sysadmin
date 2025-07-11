#!/usr/bin/env bash
packages=(
    arp-scan
    bluetooth
    default-jdk
    fd-find   # command: fdfind
    ffmpeg
    fsarchiver
    guile-3.0    # Gnu Scheme
    guile-3.0-dev
    geany
    gimp
    git
    git-extras
    gnome-system-tools
    gparted
    librsvg2-bin
    libgtk2.0-dev
    members
    mit-scheme
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
    vlc
    wl-clipboard
    xclip
    xsel
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
