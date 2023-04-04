#!/usr/bin/env bash

echo "installing wine"
wget -nc https://dl.winehq.org/wine-builds/winehq.key
apt-key add winehq.key
apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
apt update
apt install --install-recommends winehq-stable
