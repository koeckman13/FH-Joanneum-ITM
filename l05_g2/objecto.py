#! /usr/bin/python3
# @author leitner limd

class Laptop:
	color="black"
	
	def __str__(self):
		return("Color: {0} Label: {1}".format(self.color,self.label))
	
	def __init__(self,label,color="grey"):
		self.label=label
		self.color=color

mylaptop=Laptop("Toshiba")
print(mylaptop)

print("Test")