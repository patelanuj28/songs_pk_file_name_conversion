#!/usr/bin/env python

import os, sys
import os.path
import re

mypath=os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(mypath+"/songs"):
	for idx in range(len(dirnames)):
		p = re.I
		p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(.PK)|(\()|(\)|(-))')
		newname = p.sub (' ', dirnames[idx])
		p = re.compile('(\s+)')
		newname = p.sub (' ', newname)
		newname = newname.strip()
		

		os.rename(os.path.join(dirpath, dirnames[idx]), os.path.join(dirpath, newname))
		dirnames[idx] = newname
		print newname
