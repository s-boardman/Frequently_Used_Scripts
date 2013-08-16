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

r = 'Q:/DNA/DNA Research Data/Deafness HaloPlex/HaloPlex 2013 45x/HALOPLEX_RESULTS_LAMPROS/z_SB manipulation/Coverage/raw per base/' #specified directory
pattern = '*_15x.csv' #need to figure out how to use NOT function to remove csvs or sample file types


input_list = []
for path, dir, files in os.walk(r): #create list with filepaths + names of text files
    for name in files: #look at filenames in specified directory
        if fnmatch.fnmatch(name, pattern): #if the filename matches the pattern
            f = os.path.join(path, name) #join filepath and filename
            input_list.append(f) #add joined filepath/name to the list

#print input_list

total_bases = 268440



def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



for fil in input_list:
    print fil[139:] + '\t' + str(file_len(fil)) + '\t' + str((float(file_len(fil)/(float(total_bases))))*100) + '%'
