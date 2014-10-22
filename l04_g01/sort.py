#!/usr/bin/python3
#__author__ Viktoria, Christina

words = ["Das", "ist", "eine", "Liste"]

l = list(range(10,-10, -1))

def quad (zahl):
	return(zahl * zahl)


print(sorted(l, key = lambda zahl: zahl * zahl))
#print(sorted(words))
#print(words)

#words.sort(key = str.lower)
#print(words)
print("Test")

f = lambda x,y: x+y
print(f(2,2))