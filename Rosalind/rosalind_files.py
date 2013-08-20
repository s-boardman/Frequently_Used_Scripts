''' Working With Files
Given file with <1000 lines.
Return every 2nd line, assuming 1-based numbering of lines.
'''
f = open('F:/Misc/input.txt', 'r')
even_lines = f.readlines()[1::2]
f.close()

print even_lines

o = open('F:/Misc/output.txt','w')

for line in even_lines:
        o.write(line + '\n')
o.close()
