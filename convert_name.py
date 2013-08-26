#!/usr/bin/env python

import os, sys, glob
import os.path
import re

mypath=os.getcwd()
'''
@TODO - allow user to pass directory path from command line argument. 

'''
mypath="<absolute path of songs directory>"
try:

	for (dirpath, dirnames, filenames) in os.walk(mypath):
		for idx in range(len(dirnames)):
			p = re.I
			p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(WWW.?)|(.PK)|(\()|(\)|(-))')
			newname = p.sub (' ', dirnames[idx])
			p = re.compile('(\s+)')
			newname = p.sub (' ', newname)
			newname = newname.strip()
			
			if os.path.isdir(newname):
				pass
			else:
				os.rename(os.path.join(dirpath, dirnames[idx]), os.path.join(dirpath, newname))
				dirnames[idx] = newname
				print newname

			list_of_mp3 = glob.glob(dirpath+"/"+newname+"/*.mp3")
			for filename in list_of_mp3:
				p = re.I
				p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(.PK)|(\()|(\)|(-))|(\[)|(\])|(WWW.?)|('+newname+'\s+)')
				if os.path.basename(filename).endswith('.mp3'):
					newfilename = p.sub (' ', os.path.basename(filename))
					p = re.compile('(\s+)')
					newfilename = p.sub (' ', newfilename)
					p = re.compile('(\/\s+)')
					newfilename = p.sub ('/', newfilename)
					newfilename = newfilename.strip()
					dirname=os.path.dirname(filename)
					try :
						with open(newfilename): pass
					except IOError:
						os.rename(filename, dirname+"/"+newfilename)
					#	print 'File not exists'
					#os.rename(filename, dirname+"/"+newfilename)


except OSError as e:
	print e
