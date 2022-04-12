#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

form = cgi.FieldStorage() 

fname = form.getvalue('fname')
lname  = form.getvalue('lname')
id = form.getvalue('id')
course = form.getvalue('course')
term  = form.getvalue('term')
role = form.getvalue('role')
email = form.getvalue('email')
password  = form.getvalue('password')
confirm = form.getvalue('confirm')

r=False
if email and password and confirm and password == confirm:
    r = True
    with open('registry.csv', 'a') as f:
        f.write(fname+","+lname+","+id+","+course
        +","+term+","+role+","+email+","+password+"\n")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("</body>")
print ("</html>")








