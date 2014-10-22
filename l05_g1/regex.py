#!/usr/bin/python3
#author Pfeifer, Höffernig

import urllib.request
import re

srccode = urllib.request.urlopen("http://www.orf.at")

srccode = srccode.read()

print(re.findall("((<)/?(.*?)(>))",str(srccode))[-2][2])

print('Test')