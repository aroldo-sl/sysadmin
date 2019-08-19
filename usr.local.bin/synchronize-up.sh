## -u : update
## -p : preserve source permissions
## -g : preserve source group
## -t : preserve source time
## -r : recurse directories
## --delete : delete files that don't exist on sender
## --force : delete directories even if not empty

source_dir="$HOME/sync/"
# target_dir="aroldo@gnufix.de:/home/aroldo/sync"
target_dir="$aroldo@gnufix.de:/home/aroldo/tmp/sync"
files_from="$HOME/bin/synchronize-up-files.cfg"

rsync -uptglr  --files-from=$files_from $source_dir $target_dir
