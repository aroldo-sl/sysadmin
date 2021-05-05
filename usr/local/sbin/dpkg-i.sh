#!/usr/bin/env bash
# @file: dpkg-i.sh
# @date: 2021-05-05
# @modified: 2021-05-05
# @author: Aroldo Souza-Leite
# @comment: Installs Debian packages from /usr/local/var/deb
packages_var_dir="/usr/local/var/deb"
packages=$(ls -d $packages_var_dir/*.deb)
for package in $packages
do
	echo "installing $package"
	dpkg -i $package
done

		


