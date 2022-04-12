#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

users = []
if exists('registry.csv'):
    with open('registry.csv', 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            if not line: break
            fname, lname, id, course, term, role, username, password = line.split(',')
            users.append(','.join([username, role, course, term]))
            pass

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
for user in users:
    print ("<h2>%s</h2>" % str(user))
print ("</body>")
print ("</html>")








