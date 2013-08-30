#!/usr/bin/env python

import os, sys, glob, getopt
import os.path
import re


class clean_songs_name():

	index = 0
	rename_current_directory = False

	def __init__(self):
		self.index = 0
		#self.clean_name(path)

	
	def clean_file_name(self, dirpath, newdirname, filename):
		p = re.I
		p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(.PK)|(\()|(\)|(-))|(\[)|(\])|(www.?)|(www)|('+newdirname+')')
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
					newfilename = newdirname + index
					self.index += 1

				os.rename(filename, dirname+"/"+newfilename)
				return newfilename					

	def clean_directory_name(self, dirpath, dirname):
		p = re.I
		p = re.compile('(_)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(WWW.?)|(.PK)|(\()|(\)|(-))')
		newdirname = p.sub (' ', dirname)
		p = re.compile('(\s+)')
		newdirname = p.sub (' ', newdirname)
		newdirname = newdirname.strip()

		if os.path.isdir(newdirname):
			pass
		else:
			if newdirname == "":
				newdirname = dirname

			if self.rename_current_directory:
				os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, newdirname))
			
			return newdirname

	def clean_name(self, path):
		'''
		@TODO - allow user to pass directory path from command line argument. 

		'''
		self.path = path
		mypath = self.path
		if not os.path.isdir(mypath):
			print 'Error : Path \'' + mypath + '\' does not exists. '
			sys.exit(1)

		try:

			for (dirpath, dirnames, filenames) in os.walk(mypath):
				if len(dirnames) > 0:

					for idx in range(len(dirnames)):
						newdirname = self.clean_directory_name(dirpath, dirnames[idx])
						list_of_mp3 = glob.glob(dirpath+"/"+newdirname+"/*.mp3")
						
						for filename in list_of_mp3:
							newfilename = self.clean_file_name(dirpath, newdirname, filename)
				else:
					newdirname = os.path.basename(dirpath)
					
					newdirname = self.clean_directory_name(dirpath, os.path.basename(dirpath))


					list_of_mp3 = glob.glob(dirpath+"/*.mp3")

					self.index = 0
					for filename in list_of_mp3:
						newfilename = self.clean_file_name(dirpath, newdirname, filename)
						print newfilename


		except OSError as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hvp:v:c:",["p=","path=","version", "rename-current=", "c="])
	except getopt.GetoptError:
		print 'clean_songs_name.py -p <directory path> -v <version>'
	 	sys.exit(2)

	print ""
	try:
		change_dirname = clean_songs_name()
		change_dirname.rename_current_directory = False
		for opt, arg in opts:
			if opt == '-h':
				print 'clean_songs_name.py -p <directory path> -v <version>'
				sys.exit()
			elif opt in ('-v', '--version'):
				print "Copyright by 	: Anuj Patel"
				print 'Version		: v1.0'
				sys.exit()
			elif opt in ('--rename-current', '-c'):
				if arg == True:
					change_dirname.rename_current_directory = True
				#sys.exit()
			elif opt in ("-p", "--path"):
				#print int(arg) + " => " + str(roman)+ " => " + int(d)
				x = change_dirname.clean_name(str(arg))
				sys.exit()
			else:
				print 'clean_songs_name.py -p <directory path> -v <version>'
				sys.exit()

	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)

if __name__ == "__main__":
	main(sys.argv[1:])



