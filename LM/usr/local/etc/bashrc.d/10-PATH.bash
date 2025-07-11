HOME_BIN="$HOME/.local/bin"
mkdir -p "$HOME_BIN"
if ! [[ $PATH =~ ^:*${HOME_BIN} ]]
then
	export PATH="$HOME_BIN:$PATH"
	echo "$HOME_BIN prepended to PATH"
else
	echo "$HOME_BIN already in the beginning of PATH"
fi
echo "PATH=$PATH"
