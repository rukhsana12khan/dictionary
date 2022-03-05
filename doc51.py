e={"a":[2,3,7,10],"b":[4,1],"c":[3,9,6]}
d={}
for i,j in e.items():
    s=[]
    for k in j:
        if k%2==0:
            s.append(k)
            e[i]=s
    d[i]=s       
print(d)


dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for i in dic:
    dic[i].clear()
print(dic)