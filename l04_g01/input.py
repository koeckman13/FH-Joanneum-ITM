#!/usr/bin/python3
#@author Pfeifer, Höffernig

import sys

words = sys.argv[1:]
anzahl=0
for word in words:
	anzahl += len(word)

print("Der Input '{inp}' besteht aus '{c:04}' Buchstaben".format(inp=words,c=anzahl))

print("Test")