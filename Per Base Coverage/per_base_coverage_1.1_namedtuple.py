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


"""
http://www.artima.com/weblogs/viewpost.jsp?thread=236637
http://stackoverflow.com/questions/9007174/what-is-the-pythonic-way-to-read-a-csv-file-header
http://stackoverflow.com/questions/5830197/python-import-file-into-namedtuple
"""