dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
s={}
for i in dic.values():
    j=0
    while j<=len(i):
        s[i]=j
        j+=1
print(s)
