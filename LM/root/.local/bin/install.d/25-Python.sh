#!/usr/bin/env bash
packages=(
python3-dev
python3-tk
python3-venv
)

for package in ${packages[*]}
do
	echo
	echo "------------------<$package>---------------------------"
	apt install -y $package
	echo "------------------</$package>--------------------------"
done
