#!/bin/bash
if [ -z "$1" ];
then
    echo "Usage: $0 <path_to_file.pdf>"
    exit 1
else
	echo "URL,STATUS_CODE,HTML_TITLE"
	for i in `strings $1 | grep http | tr "()" " " | sort -u`
	do
		code=`curl -o /dev/null -s -w "%{http_code}\n" $i`
		title=`curl "$i" -so - | grep -Eo "<title>(.*)<\/title>"`
		echo $i","$code","$title
	done
fi
