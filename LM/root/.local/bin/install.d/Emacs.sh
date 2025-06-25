#!/usr/bin/env bash

# ## https://gist.github.com/zoliky/0445b20676bfa85450d7df006066ceb7

apt build-dep emacs
apt install libtree-sitter-dev
apt install build-essential texinfo libx11-dev libxpm-dev libjpeg-dev libpng-dev libgif-dev libtiff-dev libgtk2.0-dev libncurses-dev automake autoconf
apt update -y
apt install libmagickwand-dev -y
apt install software-properties-common -y
add-apt-repository  "deb http://gb.archive.ubuntu.com/ubuntu jammy main"
apt install  libwebkit2gtk-4.0-dev
