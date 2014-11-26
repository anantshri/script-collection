#!/bin/bash
# A simple script which will loop over content of a file.
# for each line it runs the command specified in second and third options.
#
# Usage:
# loop.sh list_loop_file.txt "command_prefix " " command_suffix"
#
# Example : nikto scan
#
# loop.sh list_ip.txt "nikto.pl -host " " -port 80,443"
#
while read p;
do
  $2$p$3
done<$1
