#!/usr/bin/python

from make_json import make_json;

# convert csv to json
make_json("cgi-bin/reviews.csv", "cgi-bin/reviews.json")

reviews = []
with open('cgi-bin/reviews.csv', 'r') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        if not line: break
        split = line.split(',')
        reviews.append([split[0], split[1], split[2], split[3], split[4], split[5]])







