#!/usr/bin/python3

#error handling
#strukturieren
#parallel?
#veraenderte urls?

import urllib.request

filenames=open('url-list.txt').readlines()
imagenumber=100

for singlename in filenames:
	imagenumber+=1
	localfile="myimg_"+str(imagenumber)+".jpg"
	print("downloading "+singlename+" to file "+localfile+"...")
	
	filehandle=urllib.request.urlopen(url=singlename)
	
	outfile=open(localfile,'wb')
	outfile.write(filehandle.read())
print("Done!")
