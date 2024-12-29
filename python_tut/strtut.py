name="python"
greeting="Wel come to python"
use='''Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.'''
# print string,length of string and specifiv value by indexing
print(name,len(name),name[4])
print(greeting,len(greeting),greeting[10])
print(use,len(use))
for i in name:
    print(i)
for j in greeting:
    print(j)
for k in use:
    print(k)
# using slicing operator, use to print selective value from the string
print(name[0:7]) #print upto 0 to last-1 i.e(0 to 6)
print(name[1:])#print 0 to last
print(name[:4])#print from 0 to 3
print(name[-6:-1])#negative indexing print from -6 to -1
print(name[-5:])#print from -1 to -4
print(name[:-4])
print(greeting[:]) 
print(name[0:-2])