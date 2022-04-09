#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

form = cgi.FieldStorage() 

email = form.getvalue('email')
password  = form.getvalue('password')
confirm = form.getvalue('confirm')

r=False
if email and password and confirm and password == confirm:
    r = True
    with open('registry.csv', 'a') as f:
        f.write(email+","+password+"\n")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s</h2>" % str(r))
print ("</body>")
print ("</html>")








