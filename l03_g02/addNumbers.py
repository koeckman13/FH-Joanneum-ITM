#!/usr/bin/python3
#RWachtler, MKurzweil

import sys
slice = sys.argv[1:]
res = 0
for n in slice:
	n=int(n)
	res += n
print(res)
