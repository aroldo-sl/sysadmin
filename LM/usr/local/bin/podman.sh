#!/usr/bin/env bash
# @file: podman.sh
# @author: Aroldo Souza-Leite
# @date: 2021-07-14
# @comment: calls podman from the snap store /snap
bin=/snap/podman/389/bin
cd $bin
./podman $@
