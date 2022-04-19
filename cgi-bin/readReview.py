#!/usr/bin/python

import cgi, cgitb, csv, json
from os.path import exists
from make_json import *
cgitb.enable()

# convert csv to json
make_json('reviews.csv', 'reviews.json')
            

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>working</h2>")
print ("</body>")
print ("</html>")
