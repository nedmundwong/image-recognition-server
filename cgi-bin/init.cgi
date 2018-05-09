#! /usr/bin/env python
import sys, os
import subprocess

command = ("tar xvf ImageMagick.tgz -C /").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()
from general_function import *

if __name__ == '__main__':
	try:
		htmlTop('System Initialization')
		
		print '<h1>System Initialization</h1>'
		
		htmlTail()
	except:
		cgi.print_exception()