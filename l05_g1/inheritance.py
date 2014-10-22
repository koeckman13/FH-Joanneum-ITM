#!/usr/bin/python3
#@pfiff, christina

class Person:
	def __init__(self,name,age=20,size=10):
		self.name=name[0].upper() + name[1:]
		self._age=age
		self.__size=size
	def __str__(self):
		return "ich heiße: {}".format(self.name)
	pass

class Student(Person):
	pass

class GuiElement:
	def __init__(self, x = 0, score = 20):
		self.x = x
		self.score = score 
	def move(self):
		self.x = self.x + 10
		return self.x
	def __add__(self, other):
		return self.score + other.score


class ItStudent(Student, GuiElement):
	def __init__(self, name, x = 10):
		Student.__init__(self, name)
		GuiElement.__init__(self, x)
	pass



susi = ItStudent("Susi")
print(susi.move())
gui = GuiElement()
print(susi+gui+susi)
print(gui.move())
martin = Student("martin")
print(martin.name)
print(martin._age)
#print(martin.__size)
print(isinstance(martin,Person))

print("geht")