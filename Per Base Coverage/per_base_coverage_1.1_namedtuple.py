import csv
from collections import namedtuple

with open('F:/Scripts/Per Base Coverage/test_data.csv','rb') as fin, open('F:/Scripts/Per Base Coverage/test_data_output.csv','wb') as fout: #open output file as writeable
    fin_csv = csv.reader(fin) #define csv reader function
    fout_csv = csv.writer(fout) #define the csv writer function    
    Base = namedtuple('Base', next(fin_csv)) #create namedtuple keys from header row
    for r in fin_csv: #for each row in the file
        row = Base(r[0], *map(int, r[1:])) #keep first column data values as strings, make the rest into integers
        if row.Total_Depth < 15: #for rows with total depth <15
            fout_csv.writerow(r) #write rows to the csv ouput file



"""
http://www.artima.com/weblogs/viewpost.jsp?thread=236637
http://stackoverflow.com/questions/9007174/what-is-the-pythonic-way-to-read-a-csv-file-header
http://stackoverflow.com/questions/5830197/python-import-file-into-namedtuple
"""
