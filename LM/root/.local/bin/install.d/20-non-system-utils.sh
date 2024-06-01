#!/usr/bin/env bash
packages=(
    most
    terminator
#vimtutor # not found
#xapp #dependency error
)
for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
