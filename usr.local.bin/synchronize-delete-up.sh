## -u : update
## -p : preserve source permissions
## -g : preserve source group
## -t : preserve source time
## -r : recurse directories
## --delete : dele files that don't exist on sender
## --force : delete directories even if not empty

source_dir="$HOME/sync/"
target_dir="aroldo@gnufix.de:/home/aroldo/sync"
rsync -uptglr  --delete --force $source_dir $target_dir
