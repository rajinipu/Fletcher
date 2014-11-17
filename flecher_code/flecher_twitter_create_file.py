#!/Applications/anaconda/bin/python

import csv 
input_file = csv.DictReader(open("./Iowa.out"))

Iowa = []
for row in input_file:
    Iowa.append(row)

len(Iowa)
