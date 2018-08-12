#!/bin/bash
#
# This script helps in checking response for same url pattern over a large array of domains.
# list_of_domains = list of domains without http or https section so http and https both are checked
# url_portion = "portion of url to check"
# Example
# ./check_bulk_response.sh list_domains.txt "Administrator/index.php"
# 
echo "Bulk Response checker by Anant Shrivastava"
if [ $# -eq 2 ]
then
  while read p;
  do
  curl -sL -w "%{http_code} %{url_effective}\\n" "http://$p/$2" -o /dev/null
  curl -sL -w "%{http_code} %{url_effective}\\n" "https://$p/$2" -o /dev/null
  done<$1
else
  echo "Usage example : $0 list_of_domains url_portion"
fi
