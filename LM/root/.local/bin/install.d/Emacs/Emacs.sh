#!/usr/bin/env bash

# ## https://gist.github.com/zoliky/0445b20676bfa85450d7df006066ceb7

apt build-dep emacs
add-apt-repository  "deb http://gb.archive.ubuntu.com/ubuntu jammy main"
apt update -y
