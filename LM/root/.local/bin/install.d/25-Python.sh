#!/usr/bin/env bash
##  ##https://devguide.python.org/getting-started/setup-building/index.html#deps-on-linux
##  ##https://doc.pypy.org/en/latest/build.html
##  ##https://solarianprogrammer.com/2017/06/30/building-python-ubuntu-wsl-debian/
packages=(
build-essential 
gcc 
gdb 
lcov 
libbz2-dev
libdb5.3-dev
libexpat1-dev
libffi-dev
libgc-dev 
libgdbm-compat-dev 
libgdbm-dev
liblzma-dev
libmpdec-dev
libncurses5-dev
libncursesw5-dev
libreadline-dev
libreadline6-dev 
libsqlite3-dev
libssl-dev
lzma 
lzma-dev 
make 
pkg-config 
python-cffi 
python3-dev
python3-tk
python5-venv
tk-dev 
uuid-dev
zlib1g-dev
)

for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
