#!/usr/bin/python3
#Paul, Georg

numbers=list(range(1,101))

def evenfilter(a):
	return not a%2

print(list(filter(evenfilter, numbers)))


def starmapper(a):
	return a*"*"

print(list(map(starmapper, numbers)))

print('Done')