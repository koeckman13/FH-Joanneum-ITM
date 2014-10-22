#!/usr/bin/python3
#author leitner mitterer

class Paper():

	def __init__(self,text):
		self.text=text


class Timer():
	
	def __init__(self, time):
		self.time=time
	
class Securepaper(Paper, Timer):
	
	def __init__(self, encryptiontype, text, time):
		Paper.__init__(self,text)
		Timer.__init__(self,time)
		self.encryptiontype = encryptiontype
		
	def __add__(self, other):
		sRet= Securepaper(	self.encryptiontype,
							self.text+other.text,
							(self.time+other.time)/2)
		
		return sRet
	
	def __str__(self):
		return "SecurePaper: Enc: {0}, Text: {1}, Time: {2}".format(
					self.encryptiontype,
					self.text,
					str(self.time))


s1 = Securepaper("md5","Gruppe 1",5)
s2 = Securepaper("md5","Gruppe 2",12)
s3 = Securepaper("md5","Gruppe x",1)
print(s1 + s2 + s3)