echo "sourcing usr_local_etc_bash.bashrc"
export BASHRC_DIR=/usr/local/etc/bashrc.d
if [[ -d $BASHRC_DIR ]]
	then
		for script in $(ls $BASHRC_DIR/*.bash)
			do
				echo "sourcing $script"
				source $script
			done
	else
		echo "$BASHRC_DIR missing"
fi
	

