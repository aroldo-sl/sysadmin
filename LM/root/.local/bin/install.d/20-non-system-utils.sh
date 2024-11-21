#!/usr/bin/env bash
packages=(
#vimtutor # not found
#xapp #dependency error
ffmpeg
geany
librsvg2-bin
most
pandoc
qtcreator
terminator
)

for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
