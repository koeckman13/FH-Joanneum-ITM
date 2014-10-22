#!/usr/bin/python3
#author Denise, Kevin

import sys
iv=sys.argv[1:]
x=0
for z in iv:
	print(z)
	x += int(z)
print("ergebnis", x)