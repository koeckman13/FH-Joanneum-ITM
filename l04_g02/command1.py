#!/usr/bin/python3
#@sakaijun13, taucherp13
import sys

print("Erstes Beispiel")


def formator (words, indent=4,char=' '):
	sentence=" ".join(words)
	count = len(words)
	result = "{i}Der Satz '{s}' enthält '{wc:07.5f}' Worte".format(
		wc=float(count),
		s=sentence,
		i=(char*indent))
	return result.capitalize()
words = sys.argv[1: ]
print(formator(words,char= '->'))
