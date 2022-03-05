dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
b={}
for i in dic1:
    for j in dic2:
        if i==j:
            b[i]=dic1[i]+dic2[j]
        else:
            b.update(dic1)
            b.update(dic2)
            b.update(dic3)    
print(b)        