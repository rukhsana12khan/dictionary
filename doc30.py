dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i,j in dic.items():
    for x in ' ':
       i=i.replace(x,"")
       d[i]=j
print(d)      
