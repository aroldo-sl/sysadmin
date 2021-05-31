#!/usr/bin/env bash
emacsclient --socket-name=$USER -a "" -nw  $@ .
