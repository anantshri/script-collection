#!/usr/bin/python
# custom encoder and decoder. just define your input and corresponding output elements
# put input text in text.txt and let it run.
import sys
input="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output="EMKIPUVGRXYZJWCSHBTFQANDLO"
input_lower=input.lower()
output_lower=output.lower()
print input
print output
print input_lower
print output_lower
#read file 
with open("text.txt","r") as f:
        while True:
  	c=f.read(1)
		if not c:
			break
		if c.isalpha():
			# do the conversion.
			if c.isupper():
				#replace with upper case entries
				sys.stdout.write(output[input.index(c)])
			else:
				#replace with lowercase entries
				sys.stdout.write(output_lower[input_lower.index(c)])
		else:
			sys.stdout.write(c)
