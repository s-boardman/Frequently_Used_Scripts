import csv

from collections import OrderedDict

with open("Q:/DNA/DNA Research Data/Deafness HaloPlex/HaloPlex 2013 45x/HALOPLEX_RESULTS_LAMPROS/coverage/130514_L1_L2_Deafness_17_CACTTCGA_342_785", 'rb') as fin:
    reader = csv.DictReader(fin) #reader object which iterates over a csv file(f)
    headers = reader.next() #assign the first row to the headers variable
    rows = [row for row in reader if row['Total_Depth'] == '0'] #return all rows where Total_Depth is '0'

"""for row in rows:
    print row"""


with open("C:/Documents and Settings/BoardmanS/Desktop/Scripts/Per Base Coverage/actual_data_output.csv", 'wb') as fout:
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames) #writer object which iterates over a csv file (fout) and pulls fieldnames from input file.
    headers = {} #empty dictionary for headers
    for n in writer.fieldnames: #iterate over fieldnames
        headers[n] = n #store each fieldname in the dictionary
    writer.writerow(headers) #write headers as first row in output file.
    for row in rows: #write rows from stored row dictionary to file
        writer.writerow(row)
    
#http://stackoverflow.com/questions/2982023/writing-header-in-csv-python-with-dictwriter useful answer
