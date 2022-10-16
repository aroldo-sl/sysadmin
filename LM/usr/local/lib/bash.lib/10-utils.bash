#!/usr/bin/env bash
# @file: utils-01.bash
# @description: Basic Bash utilities
# @author: Aroldo Souza-Leite
# @date: 2021-04-17
# @modified: 2021-04-17


## A shortcut for emaclient.
## Starts the emacs daemon if it ist not up yet.
emoritz (){
    emacsclient -a "" -nw $@
    }

timestamp (){
    date +"%FT%H-%M-%S"
}
