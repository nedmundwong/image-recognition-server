#! /usr/bin/env python

import cgi

from upload_function import *
from photoedit_function import *

htmlTop('Upload Image Result')
print '<h1>Upload Image</h1>'
uploadresult = save_uploaded_file()

htmlTail()