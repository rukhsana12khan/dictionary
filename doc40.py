a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
s=[]
for i in a:
    e={}
    for j in b:
        f={}
        for k in c:
            f[j]=k
            e[i]=f
            s.append(e)
            c.remove(k)
            break
        b.remove(j)
        break
print(s)    