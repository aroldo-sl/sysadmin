#!/usr/bin/env bash
# @file: restic-backup.sh
# @author: Aroldo Souza-Leite
# @date: 2021-05-15
# @modified: 2021-05-15
# @comment: configured restic backup call
repo=$(ls -d $(pwd)/repo)
echo "repository:$repo" >&2
tag=$(hostname)
backup_exclude_file=$(ls -d $(pwd)/backup-exclude.txt)
echo "backup exclude file:$backup_exclude_file" >&2
cmd="restic -r $repo backup / -x --tag $tag --exclude-file $backup_exclude_file --verbose=2"
echo $cmd
# eval $cmd