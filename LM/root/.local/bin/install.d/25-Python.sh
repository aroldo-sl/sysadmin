#!/usr/bin/env bash
##  ##https://devguide.python.org/getting-started/setup-building/index.html#deps-on-linux
##  ##https://doc.pypy.org/en/latest/build.html
##  ##https://solarianprogrammer.com/2017/06/30/building-python-ubuntu-wsl-debian/
packages=(
    build-essential
    bzip2
    gcc 
    gdb 
    lcov 
    libbz2-dev
    libdb5.3-dev
    libexpat1-dev
    libgc-dev 
    libgdbm-compat-dev 
    libgdbm-dev
    libmpd-dev
    libncurses5-dev
    libncursesw5-dev
    libreadline-dev
    libreadline6-dev 
    libsqlite3-dev
    libssl-dev
    lzma 
    lzma-dev 
    make
    openssl
    patch
    pkg-config 
    python3-cffi 
    python3-dev
    python3-tk
    python3-venv
    sqlite3
    tk-dev
    uuid-dev
#   xz #ERROR
    zlib1g-dev
)

for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
