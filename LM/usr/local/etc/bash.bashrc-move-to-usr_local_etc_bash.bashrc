export LOCAL_BASH_LIB=/usr/local/lib/bash.d
if [[ -d $LOCAL_BASH_LIB ]]
	then
		for script in $(ls $LOCAL_BASH_LIB/*.bash)
			do
				echo "sourcing $script"
				source $script
			done
fi
	

