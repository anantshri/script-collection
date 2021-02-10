#!/usr/bin/python
import sys
import argparse
import string

def cust_rot(str,rot):
  #print str
	#print rot
	output=""
	for x in range(0,len(str)):
		#print str[x]
		resp=""
		m=ord(str[x])
		if (91>m>64):
			resp=chr(ord(str[x]) + rot)
			if (ord(resp) > 90):
				resp=chr(ord(resp) - 26)
		elif (123>m>96):
			resp=chr(ord(str[x]) + rot)
			if (ord(resp) > 122):
				resp=chr(ord(resp) - 26)
		else:
			resp=str[x]
		output+=resp
	return output
def main(argv):
    target=''
    desc="""This program is used to print all possible rot combinations for alphabets only 0-25"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--string",help="Provide URL",dest='encode',required=True)
    parser.add_argument("--rot",help="[Optional] Rotation count",dest='roter',required=False)
    x=parser.parse_args()
    encode=x.encode
    roter=x.roter
    print "String :   " + encode
    if (roter is None):    
	for i in range(1,26):
		print "ROT " + str(i).zfill(2) + " :   " + cust_rot(encode,i)
    else:
	rot=int(roter)
	if (26>rot>0):
		print "ROT " + str(rot).zfill(2) + " :   " + cust_rot(encode,rot)



if __name__ == "__main__":
   main(sys.argv[1:])
