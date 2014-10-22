#!/usr/bin/python3
#@sakaijun, taucherp

#print("Hallo")


def generator(s):
	slist=s.split()
	for el in slist:
		yield(el)
	#yield(slist)	
	
g=generator("Heute ist das Wetter nicht schoen")
for a in g:
	print(a)