#! /usr/bin/python3
# @author Taucher Savovich

class GameElement:
	
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __str__(self):
		return("X:{0},Y:{1}".format(self.x,self.y))

	def move(self, dx=5, dy=0):
		self.x += dx
		self.y += dy	
		return self 
		
myGameElement=GameElement(10,20)
print(myGameElement)
print(myGameElement.move())

class ElectronicDevice:
	pass

class Computer(ElectronicDevice):
	#color="black"
	
	#constructor
	def __init__(self,ctype,os,label,color="grey"):
		self.ctype=ctype
		self.os=os
		self.label=label
		self.color=color
	
	#print (like toString)
	def __str__(self):
		return("Color: {0} Label: {1}".format(self.color,self.label))
	


class Laptop(Computer,GameElement):
	
	#constructor
	def __init__(self,ctype,os,label,color="grey",battery="5000mAh"):
		Computer.__init__(self,ctype,os,label,color="grey") #super constructor
		GameElement.__init__(self,x=0,y=0)
		self.battery=battery
	
	def __str__(self):
		return("cType:{ct}, OS:{os},Label:{lbl},Color:{c},Battery:{b}".format(
			ct=self.ctype,
			os=self.os,
			lbl=self.label,
			c=self.color,
			b=self.battery
			))
	
		
myLaptop=Laptop("Ultrabook","Win7","Samsung","green","40000mAh")
print(myLaptop)
print(myLaptop.move())




		
		
