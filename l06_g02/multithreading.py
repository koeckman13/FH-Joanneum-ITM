#!/usr/bin/python3
#@author Wachtler, Kurzweil

import threading, time
from random import randint

class Result:
	sum=0

class Biker(threading.Thread):
	def __init__(self, number, res, alock):
		threading.Thread.__init__(self)
		self.number = number
		self.res = res
		self._lck = alock
		
	
	def run(self):
		print("Biker {0} started".format(self.number))
		curtime = 2+randint(1,5)
		self._lck.acquire()
		#self.res.sum += curtime
		tmp = self.res.sum
		time.sleep(curtime)
		self.res.sum = tmp+curtime
		self._lck.release()
		print("Race finished by Biker: {0}".format(self.number))
		

bikers = {}
r = Result()
l = threading.Lock()

for i in range(1,4):
	biker = Biker(i, r, l)
	bikers[i] = biker
	biker.start()
	

for b in bikers.values():
	b.join()
	
print("Race finished")

print(r.sum)