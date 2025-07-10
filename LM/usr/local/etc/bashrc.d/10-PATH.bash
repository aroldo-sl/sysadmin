echo  "beginning of 10-PATH.bash"
mkdir -p "$HOME/.local/bin"
HOME_BIN=$HOME/.local/bin
if ! [[ $PATH =~ :*${HOME_BIN} ]]
then
	export PATH==$HOME_BIN:$PATH
	echo "$HOME_BIN added to PATH"
else
	echo "$HOME_BIN already in PATH"
fi
echo "end of 10-PATH.bash"
