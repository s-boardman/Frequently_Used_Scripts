#file input/reading

import csv

f = open("C:/Documents and Settings/BoardmanS/Desktop/Scripts/Per Base Coverage/test_data.csv", 'rb')
reader = csv.reader(f) #reader object which iterates over a csv file(f)
headers = reader.next() #assign the first row to the headers variable
#print headers
column = {} #list of columns
for h in headers: #for each header
	column[h] = []
#print column
for row in reader():
        r = zip(headers, row)
        if r['Total_Depth'] == 0:
                for h, v in r:
                        column[h].append(v)


	#for h, v in zip(headers, row): #combine header names with row values (v) in a series of tuples
	#	column[h].append(v) #append each value to the relevant column


"""
print column
print column['Locus']
print column['Total_Depth']
print column['Average_Depth_sample']
"""

#pull out bases with 0 read depth




#write base properties into a new file (put them into a new list), to be read as a CSV
