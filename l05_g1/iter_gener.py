#!/usr/bin/python3
#author Köck, Krenn

def charseq():
	a=0
	b=1
	while(b<200):
		yield a+b
		c=a+b
		a=b
		b=c

for el in charseq():
	print('{}\n'.format(el))


print('Test')