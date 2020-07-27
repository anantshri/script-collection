#!/usr/bin/env python3
import sys
import argparse
import re

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

def check(Ip):
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex, Ip)):  
        return True  
    else:  
        return False  

def main(argv):
    target=''
    hax=''
    desc="""This program is used to print various encoded values for the IP Address provided"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--ip",help="Provide IP v4 Address",dest='input',required=True)
    x=parser.parse_args()
    input=x.input
    pos=[0,0,0,0]
    if(check(input)):
        ip_array=input.split(".")
        print(ip_array)
        pos[3]=(int(ip_array[3])*1)
        pos[2]=(int(ip_array[2])*256)
        pos[1]=(int(ip_array[1])*256*256)
        pos[0]=(int(ip_array[0])*256*256*256)
        print(pos)
        print("possible DWORD entries")
        print(int(pos[3])+int(pos[2])+int(pos[1])+int(pos[0]))
        print(ip_array[0] + "." + str(int(pos[3])+int(pos[2])+int(pos[1])))
        print(ip_array[0] + "." + ip_array[1] + "." + str(int(pos[3])+int(pos[2])))
        print(ip_array[0] + "." + ip_array[1] + "." + ip_array[2] + "." +  str(pos[3]))
    else:
        print("Invalid input program only accepts IPv4 Address")


if __name__ == "__main__":
   main(sys.argv[1:])
