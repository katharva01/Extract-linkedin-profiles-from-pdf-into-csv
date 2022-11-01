import PyPDF2
import re
import sys

input= sys.argv[1]
output= sys.argv[2]

a = PyPDF2.PdfFileReader(input)

f=open('temp.txt','w')
for i in range(0,a.getNumPages()):
  str=a.getPage(i).extractText()
  f.write(str)
f.close()


f= open('temp.txt','r')
list=f.read().split('\n')
f.close()
# print(list)

nf=open(output,'w')
ar=[]
for line in list:
  if(re.findall("2nd$",line)):
    ind=(list.index(line))
    ar.append(line + ","+list[ind+1]+","+list[ind+2]+","+list[ind+3])

for item in ar:
  nf.write(item+"\n")
# print(ar)
nf.close()
  


  
