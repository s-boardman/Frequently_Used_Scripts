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

poor_coverage = {} #storage for rows with poor coverage

with open('F:/Scripts/Per Base Coverage/test_data.csv') as f:
    f_csv = csv.reader(f) #read using csv.reader()
    Base = namedtuple('Base', next(f_csv)) #create namedtuple keys from header row
    for r in f_csv: #for each row in the file
        row = Base(r[0], *map(int, r[1:]))
        """iterate over each Row in the file and assign comma seaprated values to each corresponding namedtuple key
        First column kept as a string, second column onwards processed as an ineger.
        """
        if row.Total_Depth < 15:
            (row) # somehow store rows in poor_coverage data structure to be used by a write function

print poor_coverage

"""
http://www.artima.com/weblogs/viewpost.jsp?thread=236637
http://stackoverflow.com/questions/9007174/what-is-the-pythonic-way-to-read-a-csv-file-header
http://stackoverflow.com/questions/5830197/python-import-file-into-namedtuple
"""
