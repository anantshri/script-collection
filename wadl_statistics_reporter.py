#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import httplib
import sys
#print sys.argv
def read_url(type,host,url):
	if type == "https":
		conn = httplib.HTTPSConnection(host,timeout=30)
	else:
		conn = httplib.HTTPConnection(host,timeout=30)
	
	try:
		conn.request('GET',url)
	except:
		 print 'connection fail'
	return conn.getresponse().read()

if len(sys.argv) == 4:
	type=sys.argv[1]
	host=sys.argv[2]
	url=sys.argv[3]
	link_read=read_url(type,host,url)
	souper=BeautifulSoup(link_read)
	x=souper.findAll("method")
	a=1
	get=0
	post=0
	put=0
	delete=0
	paramcount=0
	print "S.No. , Type, method name, parameter count"
	for m in x:
	    print str(a) + " " + m['name'] + " " + m['id'] + " " + str(len(m.findAll("param")))
	    paramcount = paramcount + len(m.findAll("param"))
	    if m['name'] == "POST":
		post= post+1
	    elif m['name'] == "GET":
		get=get+1
	    elif m['name'] == "PUT":
		put=put+1
	    elif m['name'] == "DELETE":
		delete=delete+1
	    a=a+1
	    
	print "GET : " + str(get)
	print "POST : " + str(post)
	print "PUT : " + str(put)
	print "DELETE : " + str(delete)

	y=souper.findAll("param")
	print "Total Method : " + str(len(x))
	print "Total Param : " + str(len(y)) + "  " + str(paramcount)
	print "Average Parameter count : " + str(len(y)/float(len(x))) 
else:
	print "========================="
	print " WADL statistic reporter"
	print "========================="
	print "Display stats about WADL"
	print "Usage is : " + sys.argv[0] + " HTTP/HTTPS HOST_NAME URL"
	print "Example : " + sys.argv[0] + " http google.com /path/to/wadl.wadl"
	exit()