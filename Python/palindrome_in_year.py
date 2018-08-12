#!/usr/local/bin/python
#identify the total number of palindrom in a year
# to loop over multiple year use this
# for i in {2015..2050}; do python palindrome_in_year.py --year $i; done | grep "^Palindrome"
import sys
import argparse
def print_pal(year,out):
    pal=0
    output=""
    if len(year) == 4 or len(year) == 2:
        if out== "print":
            print "For year " + year + " values of palindroms are listed below"
        for x in range(1,13):
            for y in range(1,32):
                if y == 31 and x in (2,4,6,9,11):
                    continue
                if x == 2 and y > 29:
                    continue
                string=str(y).zfill(2) + str(x).zfill(2) + year
                if string == string[::-1]:
                    pal = pal + 1
                    if out == "print":
                        print "Palindrome:" + string
                    else:
                        output = string + "\n" + output
        if pal == 0:
            if out == "print":
                print "No Palindrome found"
            else:
                output = "0"
    else:
        if out == "print":
            print "Year should be 4/2 characters"
        else:
            output = "0"
    if out != "print":
        return output

def main(argv):
    desc="""Identifies all possible palindrome in a year"""
    epilog="""Credit (C) Anant Shrivastava http://anantshri.info"""
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--year",help="Provide the Target year",dest='target',required=True)
    x=parser.parse_args()
    year=x.target
    print_pal(year,"print")


if __name__ == "__main__":
   main(sys.argv[1:])%
