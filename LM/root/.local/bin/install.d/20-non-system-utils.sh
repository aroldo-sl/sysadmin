#!/usr/bin/env bash
packages=(
#most
#terminator
#vimtutor # not found
#xapp #dependency error
librsvg2-bin
pandoc
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
