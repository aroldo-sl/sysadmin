#!/usr/bin/env bash
hg_revision=$(hg id -q)
archive_path="$(hg root)-$(date +'%F-%S')@$hg_revision.tar.bz2"
hg archive $archive_path
echo $archive_path
