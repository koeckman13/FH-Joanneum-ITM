#!/usr/bin/python3
#@mayerhfl13, kurzweim13

lorem="""Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
 sed diam nonumy eirmod tempor invidunt ut labore et dolore magna
  aliquyam erat, sed diam voluptua. At vero eos et accusam et
   justo duo dolores et ea rebum. Stet clita kasd gubergren,
    no sea takimata sanctus est Lorem ipsum dolor sit amet.
     Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
      sed diam nonumy eirmod tempor invidunt ut labore et 
       magna aliquyam erat, sed diam voluptua. At vero eos et
        accusam et justo duo dolores et ea rebum. Stet clita kasd
         gubergren, no sea takimata sanctus est Lorem ipsum dolor
          sit amet. """
def fiveLetterFilter(word):
	return len(word)>4
	
sortedLorem=sorted(list(filter(lambda x:len(x)>4,lorem.split())))
print(sortedLorem)

def makeHTML(word):
	return "<{tag}>{w}</{tag}>".format(tag="p",w=word)
	
print(list(map(makeHTML,lorem.split())))
import re
re.findall(r'\d+','heute ist 06.Oktober 2014')