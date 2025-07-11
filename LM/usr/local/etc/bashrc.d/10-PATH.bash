HOME_BIN="$HOME/.local/bin"
mkdir -p "$HOME_BIN"
if ! [[ $PATH =~ ^:*${HOME_BIN} ]]
then
	export PATH="$HOME_BIN:$PATH"
fi
echo "PATH=$PATH"
