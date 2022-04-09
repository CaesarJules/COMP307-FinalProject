import csv
from os.path import exists

# r = False
# if exists('registry.csv'):
#     with open('registry.csv', 'r') as f:
#         for line in f.readlines():
#             line = line.strip()
#             stored_email, stored_password = line.split(',')
#             print(stored_email, stored_password)
#             if stored_email == "adrien@gmail.com" and stored_password == "asdf":
#                 r = True

# print(r)

email = "new@gmail.com"
password = "234"
confirm= "234"

with open('registry.csv', 'a') as f:
    f.write(email+","+password+"\n")