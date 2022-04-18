#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

reviews = []
with open('reviews.csv', 'r') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        if not line: break
        split = line.split(',')
        reviews.append([split[0], split[1], split[2], split[3], split[4], split[5]])
            

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
for review in reviews:
    print ("<h2>%s</h2>" % str(review)) 
print ("</body>")
print ("</html>")








