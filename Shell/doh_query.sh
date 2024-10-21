#!/bin/bash
# Script by Anant Shrivastava (https://anantshri.info)
echo "Script to validate DoH Queries"

print_header() {
    printf "%-15s %-25s\n" "Provider" "Resolved Data"
    echo "----------------------------------------------"
}

print_row() {
    printf "%-15s %-25s\n" "$1" "$2"
}

# Define an array of providers with their details
providers=(
    "CloudFlare|https://cloudflare-dns.com/dns-query?name={domain}"
    "Quad9|https://dns.quad9.net:5053/dns-query?name={domain}"
    "GoogleDNS|https://dns.google/resolve?name={domain}"
    "DNS0.eu|https://dns0.eu/dns-query?name={domain}"
    # Add more providers as needed

)


if [ $# -eq 1 ]; then
    domain=$1
    echo "DNS Resolution for: $domain"
    echo ""
    print_header


    for provider in "${providers[@]}"; do
        IFS='|' read -r name url_template <<< "$provider"
        url="${url_template//\{domain\}/$domain}"

        # Fetch and parse the DNS response
        response=$(curl -s --http2 --header "accept: application/dns-json" "$url")
        resolved_data=$(echo "$response" | jq -r '.Answer[]?.data' | paste -sd "," -)

        print_row "$name" "$resolved_data"
    done
else
    echo "Usage: $0 <domain name>"
fi
