#!/usr/bin/python
import sys
import argparse
import hashlib
import base64

def main(argv):
    target=''
    hax=''
    desc="""This program is used to print various encoded and encrypted version of the same string"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--string",help="Provide URL",dest='input',required=True)
    parser.add_argument("--type",help="[Optional] Type of Encoding / Encryption",dest='type',required=False)
    x=parser.parse_args()
    input=x.input
    type=x.type
    #print hashlib.algorithm_available
    print "Input  : " + input.encode()
    print "***************  Various Bases  ******************************"
    print "Binary : " + ' '.join(format(ord(x), 'b') for x in input) 
    print "Octal  : " + ' '.join(format(ord(a),'o') for a in input)
    print "Hex    : " + ' '.join(format(ord(a),'x') for a in input)
    print "***************  Common Hashes  ******************************"
    print "MD5    : " + hashlib.md5(input.encode()).hexdigest()
    print "SHA1   : " + hashlib.sha1(input.encode()).hexdigest()
    print "SHA224 : " + hashlib.sha224(input.encode()).hexdigest()
    print "SHA256 : " + hashlib.sha256(input.encode()).hexdigest()
    print "SHA384 : " + hashlib.sha384(input.encode()).hexdigest()
    print "SHA512 : " + hashlib.sha512(input.encode()).hexdigest()
    print "***************  Various Encodings ****************************"
    print "Base64 : " + base64.b64encode(input.encode())
    print "Base16 : " + base64.b16encode(input.encode())
    print "Base32 : " + base64.b32encode(input.encode())

if __name__ == "__main__":
   main(sys.argv[1:])