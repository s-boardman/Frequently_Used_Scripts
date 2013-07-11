"""a script to append the contents of a series of text documents into a single large document
All input documents have the same number of columns and are tab delimited"""

import os
from fnmatch import fnmatch

r = 'Q:/DNA/DNA Research Data/Deafness HaloPlex/HaloPlex 2013 45x/HALOPLEX_RESULTS_LAMPROS/alamut-ht/Homozygous Recessive Mutations - Putative'
pattern = 'Sample **.txt'


input_list = []
for path, dir, files in os.walk(r): #create list with filepaths + names of text files
    for name in files:
        if fnmatch(name, pattern):
            f = os.path.join(path, name)
            input_list.append(f)

#print input_list

fout = open("C:/Documents and Settings/BoardmanS/Desktop/Scripts/test_concatenator.txt","a")

for file_ in input_list: #This creates a file with *all* the lines; I want to ignore the first line (which contains the headers).
    fin = open(file_, 'r')
    contents = fin.read() #can I read from the second line in the file?
    fout.write(contents)
fout.close()

output_file = open("C:/Documents and Settings/BoardmanS/Desktop/Scripts/Variant Concatenator/test_concatenator_cleaned.txt","w")
with open("C:/Documents and Settings/BoardmanS/Desktop/Scripts/Variant Concatenator/test_concatenator.txt","r") as input_file:
    lines = input_file.readlines() #read lines in concatenated file
    for line in lines: #for each line
        if line.startswith("ID"): #for lines with headers (matches ID etc)
            output_file.write("\n") #write a new line (removes header line)
        else: #for all other lines (i.e. variant lines)
            output_file.write(line) #write the line as is
input_file.close()
          
"""
Next step is to add in sample names in place of header rows.
Also need to add in overall header row.
"""
