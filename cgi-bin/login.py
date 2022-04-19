#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

form = cgi.FieldStorage() 

email = form.getvalue('email')
password  = form.getvalue('password')


r = False
role = ''
if exists('/home/2019/aphila/public_html/cgi-bin/registry.csv'):
    with open('/home/2019/aphila/public_html/cgi-bin/registry.csv', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line: break
            _,_,_,_,_,stored_role,stored_email, stored_password = line.split(',')
            if stored_email == email and stored_password == password:
                r = True
                role = stored_role

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s</h2>" % str(r))
print ("<h2>%s</h2>" % role)
print ("</body>")
print ("</html>")








