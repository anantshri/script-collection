#!/usr/bin/python
# A simple python script to extract host information from shodan
# Requires a API_KEY from shodan.io
# and shodan python module : easy_install shodan
# Created by Anant Shrivastava https://anantshri.info
# Sample Usage
'''
$python shodan_ip.py 8.8.8.8 2>/dev/null

        IP: 8.8.8.8
        Organization: Google
        Operating System: None

Port: 53 ;
        Banner: 1a648183000100000001000002383303323133033136340331313207696e2d61646472046172706100000c0001c0130006000100000707002f016703646e73026b720007696e7665727365036e6963026f72c03f77fd2c19000054600000038400093a800000a8c0
'''
#
import sys
import shodan
api = shodan.Shodan('API_KEY_HERE')
vulncnt=0
if len(sys.argv) > 1:
    #print "Lets check api"
    host = api.host(sys.argv[1])

    # Print general info
    print """
        IP: %s
        Organization: %s
        Operating System: %s
    """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
    # Print all banners
    # Print all Vuln's caught by Shodan
    print "Vulnerabilities: "
    for vuln in host['vulns']:
        if vuln.find("!") == -1:
            vulncnt = vulncnt + 1
            print "**  " + vuln + "  **"
    if vulncnt == 0:
        print "No Vulnerability picked by Shodan"
    print ""
    for item in host['data']:
            print """Port: %s ;
        Banner: %s""" % (item['port'], item['data'])
else:
    exit
