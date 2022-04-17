#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

form = cgi.FieldStorage() 

course_nb = form.getvalue('course-nb')
term  = form.getvalue('term')
star = form.getvalue('star')
review = form.getvalue('review')
ta_name = form.getvalue('ta_name')
ta_id = form.getvalue('ta_id')

with open('/home/2019/aphila/public_html/cgi-bin/reviews.csv', 'a') as f:
    f.write(term+","+course_nb+","+ta_name+","+ta_id+","+star+","+review+"\n")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("</body>")
print ("</html>")