#!/bin/bash
echo "Script to validate DoH Queries"
print_header() {
    printf "%-15s %-15s %-25s\n" "Provider" "DNS IP" "Resolved data"
    echo "---------------------------------------------------------"
}
print_row() {
    printf "%-15s %-15s %-25s\n" "$1" "$2" "$3"
}
if [ $# -eq 1 ]
then
	name=$1
	echo "DNS Resolution for : $name"
	echo ""
	print_header
	print_row "CloudFlare" "1.1.1.1" $(curl -q --http2 --header "accept: application/dns-json" "https://cloudflare-dns.com/dns-query?name=$name" 2>/dev/null | jq '.Answer[]?.data' -r)
	print_row "Quad 9" "9.9.9.9" $(curl -q --http2 --header "accept: application/dns-json" "https://dns.quad9.net:5053/dns-query?name=$name" 2>/dev/null | jq '.Answer[]?.data' -r)
	print_row "Google DNS" "8.8.8.8" $(curl -q --http2 --header "accept: application/dns-json" "https://dns.google/resolve?name=$name" 2>/dev/null | jq '.Answer[]?.data' -r)
	print_row "DNS0.eu" "" $(curl -q --http2 --header "accept: application/dns-json" "https://dns0.eu/dns-query?name=$name" 2>/dev/null | jq '.Answer[]?.data' -r)

else
	echo "$0 <domain name>"
fi
