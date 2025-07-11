#!/usr/bin/env bash
## https://operavps.com/docs/fix-ubuntu-boot-problem/
## <add repositories>
add-apt-repository universe
add-apt-repository ppa:yannubuntu/boot-repair
## https://help.ubuntu.com/community/mkusb
add-apt-repository ppa:mkusb/ppa
apt update
## </add repositories>
## <packages>
apt install -y boot-repair
apt install -y mkusb
## </packages>
