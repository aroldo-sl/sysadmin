#!/usr/bin/env bash
export XDG_CONFIG_HOME="$HOME/.config"
config="$XDG_CONFIG_HOME/yt-dlp/config-herrquesada-YouTube"
export log_dir="/tmp/yt-dlp"
mkdir -p $log_dir
#
messages_log="$log_dir/messages.log"
errors_log="$log_dir/errors.log"
metadata_list="$log_dir/metadata.list"
#
function datetime {
    date_time=$(date +'%FT%T')
    date_time=${date_time//:/-}
    echo $date_time
}
#
for logfile in $messages_log $errors_log $metadata_list
do
    echo "initializing $logfile"
    echo "####DATETIME:$(datetime)" >> $logfile
done
#
/home/schlangenbrut/.local/bin/yt-dlp \
    --no-simulate \
    --print-to-file "%\(fulltitle\)s §%\(id\)s§ %\(playlist\)s" $metadata_list \
    --config $config \
    $@ \
    > >(tee -a $messages_log) 2> >(tee -a $errors_log >&2)

