#!/usr/bin/python2

import  cgi

print  "Content-type:text/html"
print   ""

web_data=cgi.FieldStorage()

out=web_data.getvalue('x')

print out




