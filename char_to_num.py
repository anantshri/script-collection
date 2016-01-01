#!/usr/bin/python -tt
import os
import argparse
import sys
def main(argv):
    total=0
    desc="""This program is used to print numeric value of character"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--string",help="Provide Input",dest='input',required=True)
    x=parser.parse_args()
    input=x.input
    #print "Input  : " + input.encode()
    for a in input:
        total = total + (ord(a.lower()) - 96)
    while (total >= 10):
        total1 = 0
        for m in str(total):
            total1 = total1 + int(m)
        total = total1
    print "Sum total : " + total
if __name__ == "__main__":
   main(sys.argv[1:])
