#!/usr/bin/env bash
## https://operavps.com/docs/fix-ubuntu-boot-problem/
add-apt-repository ppa:yannubuntu/boot-repair
apt update
apt install -y boot-repair
