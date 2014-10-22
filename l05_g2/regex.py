#!/usr/bin/python3
#__author__ Kurzweil. Wachtler

import urllib.request
import re

html = urllib.request.urlopen("http://www.smashingmagazine.com").read()
print(re.findall("(<h2><a (.*?)>(.*?)</a></h2>)", str(html))[-1][-1])
