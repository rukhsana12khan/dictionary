name="mississippi"
s={}
for i in name:
    if i in s:
        s[i]+=1
    else:
        s[i]=1    
print(str(s))