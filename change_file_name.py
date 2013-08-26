#!/usr/bin/env python
#coding: utf8 

from ID3 import *
import glob, sys, os


a=glob.glob("songs/*.mp3")
print a


from os import listdir
from os.path import isfile, join
mypath="/Users/patelanuj28/workspace/python/mp3_converter/songs"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
b=os.listdir(mypath)
print b

sys.exit()



try:
	id3info = ID3('/Users/patelanuj28/test.mp3')
	print id3info
	id3info['TITLE'] = "Green Eggs and Ham"
	id3info['ARTIST'] = "Moxy Früvous"
	for k, v in id3info.items():
		print k, ":", v
except InvalidTagError, message:
	print "Invalid ID3 tag:", message
