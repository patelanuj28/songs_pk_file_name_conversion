#!/usr/bin/env python

import os, sys, glob, getopt
import os.path
import re
current_file_name = os.path.basename(__file__)

class clean_songs_name():

	index = 0
	rename_current_directory = False

	def __init__(self):
		self.index = 0
		#self.clean_name(path)
	
	def clean_file_name(self, dirpath, filename):
		p = re.I
		p = re.compile('(_)|(2014)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(.PK)|(\()|(\)|(-))|(\[)|(\])|(www.?)|(www)')
		if os.path.basename(filename).endswith('.mp3'):
			newfilename = p.sub ('', os.path.basename(filename))
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
					newfilename = filename + self.index
					self.index += 1
			os.rename(filename, dirname+"/"+newfilename)
			print newfilename

	def clean_directory_name(self, dirpath):
		
		path = os.path.dirname(dirpath)
		dirname = os.path.basename(dirpath)
		
		if not path or not dirname:
			return
		
		p = re.I
		p = re.compile('(_)|(2014)|(2013)|(2012)|(2010)|(2011)|(2009)|(Songs)|(128)|(320)|(Kbps)|(WWW.?)|(.PK)|(\()|(\)|(-))')
		newdirname = p.sub (' ', dirname)
		p = re.compile('(\s+)')
		newdirname = p.sub (' ', newdirname)
		newdirname = newdirname.strip()

		newdirname = "%s/%s" % (path, newdirname)

		if os.path.isdir(newdirname):
			pass
		else:

			if newdirname == "":
				newdirname = dirname			
			if self.rename_current_directory:
				os.rename(dirpath, newdirname)
			
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

			for (dirpath, dirnames, filenames) in os.walk(mypath,topdown=False):				
				#if len(dirnames) > 0:
				if dirpath:
					newdirname = self.clean_directory_name(dirpath)													

			for (dirpath, dirnames, filenames) in os.walk(mypath):
				for f in filenames:
					if f.endswith(".mp3"):
						self.index = 0
						fname = "%s/%s" % (dirpath, f)
						newfilename = self.clean_file_name(dirpath, fname)										

		except OSError as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno, str(e))
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno, str(e))

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hvp:v:c:",["p=","path=","version", "rename-dir=", "c="])
	except getopt.GetoptError:
		print '%s -p <directory path> -v <version>' % current_file_name
	 	sys.exit(2)

	print ""
	try:
		change_dirname = clean_songs_name()
		
		for opt, arg in opts:
			if opt == '-h':
				print '%s -p <directory path> -v <version>' % current_file_name
				sys.exit()
			elif opt in ('-v', '--version'):
				print "Copyright by 	: Anuj Patel"
				print 'Version		: v1.1'
				sys.exit()
			elif opt in ('--rename-dir', '-c'):
				if arg.lower() == "true":
					change_dirname.rename_current_directory = True
				#sys.exit()
			elif opt in ("-p", "--path"):
				#print int(arg) + " => " + str(roman)+ " => " + int(d)
				x = change_dirname.clean_name(str(arg))
				sys.exit()
			else:
				print '%s -p <directory path> -v <version>' % current_file_name
				sys.exit()

	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno, str(e))

if __name__ == "__main__":
	main(sys.argv[1:])
