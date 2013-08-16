"""
This script takes all the files in a folder with names that fit a specified pattern and make thme into a list.
Next the list will be iterated over and for each file the data will be read into namedtuples.
For each row in the file the Total_Depth value will be analysed.
For every row with a Tota_Depth value of less than 15 the row will be output into a new file containing only these low coverage base pairs.
"""


import csv
from collections import namedtuple
import os
import fnmatch

r = 'Q:/DNA/DNA Research Data/Deafness HaloPlex/HaloPlex 2013 45x/HALOPLEX_RESULTS_LAMPROS/z_SB manipulation/Coverage/raw per base/test' #specified directory
pattern = '130514_L1_L2_Deafness_*' #need to figure out how to use NOT function to remove csvs or sample file types


input_list = []
for path, dir, files in os.walk(r): #create list with filepaths + names of text files
    for name in files: #look at filenames in specified directory
        if fnmatch.fnmatch(name, pattern): #if the filename matches the pattern
            f = os.path.join(path, name) #join filepath and filename
            input_list.append(f) #add joined filepath/name to the list

#print input_list


for fil in input_list:
    with open(fil,'rb') as fin, open(fil + '_15x.csv','wb') as fout: #open output file as writeable
        fin_csv = csv.reader(fin, dialect='excel-tab') #define csv reader function
        fout_csv = csv.writer(fout, dialect='excel') #define the csv writer function
        n = namedtuple('BasePair', next(fin_csv)) #create namedtuple keys from header row
        header = n._fields #store field names from namedtuple n as header variable
        #print header
        #print type(header)
        fout_csv.writerow(header)
        for r in fin_csv: #for each row in the file
            row = n(r[0], *map(float, r[1:])) #keep first column data values as strings, make the rest into floats
            if row.Total_Depth < 15.0: #for rows with total depth <15
                #print row
                fout_csv.writerow(r) #write rows to the csv ouput file

"""
Next steps:
Group sequential bases with poor coverage into contigs
"""
