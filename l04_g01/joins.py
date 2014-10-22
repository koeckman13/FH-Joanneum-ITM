#!/usr/bin/python3
#@author Krenn, Koeckman

import sys

words = sys.argv[1:]
#anzahl=0
#for word in words:
	#anzahl += len(word)
countSatz="".join(words)
Satz=" ".join(words)
anzahl=len(countSatz)

print("Der Input '{inp}' besteht aus '{c:04}' Buchstaben".format(inp=Satz,c=anzahl))

print("Test")