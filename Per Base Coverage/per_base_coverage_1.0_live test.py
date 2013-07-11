import csv

from collections import OrderedDict

with open("C:/Users/BoardmanS/Desktop/Haloplex 2013 Coverage/130514_L1_L2_Deafness_17_CACTTCGA_342_785", 'rb') as fin:
    reader = csv.DictReader(fin, delimiter = "\t") #reader object which iterates over a file(f) specified as tab separated
    headers = reader.next() #assign the first row to the headers variable
    rows = [row for row in reader if row['Total_Depth'] == '0'] #return all rows where Total_Depth is '0'

"""for row in rows:
    print row"""


with open("F:/Scripts/Per Base Coverage/actual_data_output.csv", 'wb') as fout:
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames) #writer object which iterates over a csv file (fout) and pulls fieldnames from input file.
    headers = {} #empty dictionary for headers
    for n in writer.fieldnames: #iterate over fieldnames
        headers[n] = n #store each fieldname in the dictionary
    writer.writerow(headers) #write headers as first row in output file.
    for row in rows: #write rows from stored row dictionary to file
        writer.writerow(row)
    
"""
Want to be able to iterate over files in a folder.
Output to different files, named after each sample.
May need to specify the file first then manually close it (ie not use "with open(etc...)
Will produce bases with 0 coverage for each sample file.
Next produce a script to concatenate all 0 coverage base.
Finally modify that script to assign a new variable to each line as the sample name for sorting and ID.
"""
