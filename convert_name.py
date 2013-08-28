#!/usr/bin/env python

import os, sys, glob, getopt
import os.path
import re


class clean_songs_name():

	def __init__(self, path):
		self.path = path
		self._clean_name(path)

	def _clean_name(self, path):
		'''
		@TODO - allow user to pass directory path from command line argument. 

		'''

		mypath = self.path
		if not os.path.isdir(mypath):
			print 'Error : Path \'' + mypath + '\' does not exists. '
			sys.exit(1)

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
						if newname == "":
							newname = dirnames[idx]

						os.rename(os.path.join(dirpath, dirnames[idx]), os.path.join(dirpath, newname))
						dirnames[idx] = newname
						print newname

					list_of_mp3 = glob.glob(dirpath+"/"+newname+"/*.mp3")
					for filename in list_of_mp3:
						p = re.I
						p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(.PK)|(\()|(\)|(-))|(\[)|(\])|(www.?)|(www)|('+newname+')')
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
								if newfilename == "":
									newfilename = newname
								os.rename(filename, dirname+"/"+newfilename)
							#	print 'File not exists'
							#os.rename(filename, dirname+"/"+newfilename)						

		except OSError as e:
			print e


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hvp:",["p=","path=","version="])
	except getopt.GetoptError:
		print 'clean_songs_name.py -p <directory path> -v <version>'
	 	sys.exit(2)

	print ""
	try: 
		for opt, arg in opts:
			if opt == '-h':
				print 'clean_songs_name.py -p <directory path> -v <version>'
				sys.exit()
			elif opt in ('-v'):
				print  " " + "-" * 50
				print "|  Copyright by 	: Anuj Patel"
				print '|  version 		: v1.0'
				print " " + "-" * 50
				sys.exit()
			elif opt in ("-p", "--path"):
				#print int(arg) + " => " + str(roman)+ " => " + int(d)
				x = clean_songs_name(str(arg))
				sys.exit()
			else:
				print 'clean_songs_name.py -p <directory path> -v <version>'
				sys.exit()

	except Exception as e:
		print e

if __name__ == "__main__":
	main(sys.argv[1:])



