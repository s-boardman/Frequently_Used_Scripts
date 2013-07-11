import csv
from collections import namedtuple

"""
with open("F:/Scripts/Per Base Coverage/test_data.csv", 'rb') as fin: #open file
	BaseData = namedtuple('BaseData', ['locus, total_depth, average_depth_sample, other_depth'], verbose=True) #construct the named tuple class and keys
	for line in map(BaseData._make, csv.reader(fin): #read the input file and then for each line
		print 'Base %s has a depth of %f' % (BaseData.locus, BaseData.total_depth) #print this statement with the relevant values.
		
"""
		
	

import csv
from collections import namedtuple

with open('F:/Scripts/Per Base Coverage/test_data.csv', mode="r") as infile:
    reader = csv.reader(infile)
    Data = namedtuple("Data", next(reader))
    for row in reader:
        data = Data(*row)
Print data	