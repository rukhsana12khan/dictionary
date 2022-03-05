dic=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
y=[]
b=[]
r=[]
s={}
for i,j in dic:
    if i=="yellow":
        y.append(j)
        s[i]=y
    if i=="blue":
        b.append(j)
        s[i]=b
    if i=="red":
        r.append(j)
        s[i]=r
print(s)                          