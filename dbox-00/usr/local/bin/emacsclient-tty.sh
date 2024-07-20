#!/usr/bin/env bash
sudo chmod a+rw $(tty)
/usr/bin/emacsclient "$@"
