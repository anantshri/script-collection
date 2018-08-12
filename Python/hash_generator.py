#!/usr/bin/env python2
import sys
import argparse
import passlib.hash 
import passlib.apps
import hashlib
import base64

def main(argv):
    target=''
    hax=''
    desc="""This program is used to print various encoded and encrypted version of the same string"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--string",help="Provide URL",dest='input',required=True)
    x=parser.parse_args()
    input=x.input
    #print hashlib.algorithm_available
    print "Input  : " + input.encode()
    print "***************  Various Bases  ******************************"
    print "Binary : " + ' '.join(format(ord(x), 'b') for x in input) 
    print "Octal  : " + ' '.join(format(ord(a),'o') for a in input)
    print "Hex    : " + ' '.join(format(ord(a),'x') for a in input)
    print "***************  Common Hashes via hashlib  ******************************"
    print "MD5    : " + hashlib.md5(input.encode()).hexdigest()
    print "SHA1   : " + hashlib.sha1(input.encode()).hexdigest()
    print "SHA224 : " + hashlib.sha224(input.encode()).hexdigest()
    print "SHA256 : " + hashlib.sha256(input.encode()).hexdigest()
    print "SHA384 : " + hashlib.sha384(input.encode()).hexdigest()
    print "SHA512 : " + hashlib.sha512(input.encode()).hexdigest()
    print "***************  Various Hashes via passlib ****************************"
    print "LM : " + passlib.hash.lmhash.hash(input.encode())
    print "NTLM : " + passlib.hash.nthash.hash(input.encode())
    print "LDAP SSHA : " + passlib.apps.ldap_context.hash(input.encode())
    print "LDAP SSHA : " + passlib.apps.ldap_context.replace(default="ldap_salted_md5").hash(input.encode())
    print "MySQL 4: " + passlib.apps.mysql_context.hash(input.encode())
    print "MySQL 3: " + passlib.apps.mysql3_context.hash(input.encode())
    print "MSSQL 2000: " + passlib.hash.mssql2000.hash(input.encode())
    print "MSSQL 2005: " + passlib.hash.mssql2005.hash(input.encode())
    print "Oracle 11: " + passlib.hash.oracle11.hash(input.encode())
    print "***************  Various Encodings ****************************"
    print "Base64 : " + base64.b64encode(input.encode())
    print "Base16 : " + base64.b16encode(input.encode())
    print "Base32 : " + base64.b32encode(input.encode())
    print "cisco Type 7: " + passlib.hash.cisco_type7.hash(input.encode())

if __name__ == "__main__":
   main(sys.argv[1:])