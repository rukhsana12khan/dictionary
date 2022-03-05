dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=[]
for x in dic.items():
    s.append(x)
    s.sort()
print(s)