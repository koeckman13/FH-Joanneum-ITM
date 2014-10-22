#!/usr/bin/python3
#@martin, georg

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

martin = Student("martin")
print(martin.name)
print(martin._age)
#print(martin.__size)
print(isinstance(martin,Person))

print("geht")