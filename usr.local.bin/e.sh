#!/usr/bin/env bash

# sets the parameter "file" to the present work directory.
echo "scrip file name:$0"

if ((${#@}<1));
    then
          set "$(pwd)"; # this sets @[0]=`pwd`, believe me!
fi;
emacs_command_input_cfg="$HOME/.emacs.d/emacs-command-input.cfg"

if [ -f "$emacs_command_input_cfg" ];
    then
    echo "using emacs command input file:$emacs_command_input_cfg";
    emacsclient -a "" -nw "$@" < "$emacs_command_input_cfg";
    else
    echo "missing emacs command input file:$emacs_command_input_cfg";
    emacsclient -a "" -nw "$@";
fi
    

