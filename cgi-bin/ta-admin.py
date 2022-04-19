#!/usr/bin/python

import cgi, cgitb
from os.path import exists
cgitb.enable()

courses = []
with open('TA_database.csv', 'r') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        if not line: break
        split = line.split(',')
        courses.append([split[1], split[2], split[4]])

TAs = []
if exists('TACohort.csv'):
    with open('TACohort.csv', 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            if not line: break
            split = line.split(',')
            for i in range(len(split)):
                split[i].strip()
            ta = [split[1].strip(),split[2].strip()]
            for course in courses:
                if course[2] == ta[1]:
                    ta.extend([course[0], course[1]])
            TAs.append(','.join(ta))
           # TAs.append(ta)
            

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
for ta in TAs:
    print ("<h2>%s</h2>" % str(ta)) 
print ("</body>")
print ("</html>")








