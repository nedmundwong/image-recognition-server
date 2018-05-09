#! /usr/bin/env python
import os, inspect, sys

import subprocess

command = ("tar xvf ImageMagick.tgz -C /").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

command = ("pip install --upgrade pip").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

command = ("pip install tensorflow==1.0.1").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

command = ("pip install keras==1.2.2").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

command = ("pip install h5py").split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
output, err = process.communicate()

command = ("wget https://s3.amazonaws.com/stratospark/food-101/model4b.10-0.68.hdf5 -P "+os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/upload").split()
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