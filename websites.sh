#!/bin/bash
run_me="/usr/bin/chromium"
home_path="~/.chromium_profiles_here/"
if [ $# -eq 1 ]
then
open_all=0
else
echo "$0 tweet|mail to open selective"
fi
if [ $1 == "help" ]
then
    echo "$0 tweet|mail"
    exit
fi
if [ $1 == "tweet" ]
then
    $run_me --app="https://tweetdeck.twitter.com" --user-data-dir=$home_path/twitter &
fi
if [ $1 == "mail" ]
then
    $run_me --disable-gpu --app="https://www.gmail.com/" --user-data-dir=$home_path/gmail &
fi
echo "Some Error Occured"
echo "$0 tweet|mail"
exit
