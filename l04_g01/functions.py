#!/usr/bin/python3
#@author Martin, Georg

import sys

words = sys.argv[1:]

def charcount(words, IgnoreWhitespaces=False):
	countSatz="".join(words)
	Satz=" ".join(words)
	if(IgnoreWhitespaces==True):
		anzahl=len(countSatz)
		z="Buchstaben"
	else:
		anzahl=len(Satz)
		z="Zeichen"
	return("Der Input '{inp}' besteht aus '{c:04}' {z}".format(inp=Satz,c=anzahl,z=z))

print(charcount(words, IgnoreWhitespaces=True))

print(charcount(words))

print("Test")