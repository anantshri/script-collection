#!/bin/bash
GREPPARAM="HTTP|Length|Content-Type:|Location"
i=0
x=${2:-0}
prot=${3:-"http"}
function check_dvcs(){
          p=$1
          i=$2
          # GIT
          echo "$i;$p/.git/HEAD;"`curl -s $prot://$p/.git/HEAD | grep "ref:"`
          # SVN
          echo "$i;$p/.svn/entries;"`curl -s -I $prot://$p/.svn/entries | egrep $GREPPARAM | tr "\r\n" ";" | tr -s ";"`
          echo "$i;$p/.svn/wc.db;"`curl -s -I $prot://$p/.svn/wc.db | egrep $GREPPARAM | tr "\r\n" ";" | tr -s ";"`
          # HG : .hg/requires
          echo "$i;$p/.hg/requires;"`curl -s -I $prot://$p/.hg/requires | egrep $GREPPARAM | tr "\r\n" ";" | tr -s ";"`
          # BZR
          # .bzr/README
          echo "$i;$p/.bzr/README;"`curl -s -I $prot://$p/.bzr/README | egrep $GREPPARAM | tr "\r\n" ";" | tr -s ";"`
}
if [ ! -f $1 ]; then
    echo "No file found"
    check_dvcs $1 $i
else
  while read p;
  do
    i=`expr $i + 1`
    if [ $i -lt $x ]
    then
          echo "$i;$p:Skipping"
    else
          check_dvcs $p $i
    fi
  done<$1
fi
