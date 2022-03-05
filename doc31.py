dic={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
smax=0
tmax=0
m=0
s=0
t=0
for i in dic:
    if dic[i]>max:
        tmax=smax
        t=s
        smax=max
        s=m
        max=dic[i]
        m=i
    if dic[i]!=max and dic[i]>smax:
        tmax=max
        t=m 
        smax=dic[i]
        s=i
    if dic[i]!=max and dic[i]!=smax and dic[i]>tmax:
        tmax=dic[i]
        t=i
print(m,s,t)        

