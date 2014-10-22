#!/usr/bin/python3
#author: Stifter, Mayerhofer

r = range(-10, 15, 4)

print(r.__iter__().__next__())

for elem in r:
	print(elem)

def idGenerator(y=2014):
	no=1
	while no<1000:
	 yield "{0}{1:03}".format(y,no)
	 no+=1
#	yield "{0}{1:03}".format(y,no)
	
g=idGenerator()
for elem in g:
 print(elem)
# print(g.__next__())
#print(g.__next__())	
#print(g.__next__())	