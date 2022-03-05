dict=[1,34,7,9]
dict1=[2,5,6,"rukko"]
s={}
for i in dict:
    for j in dict1:
        s[i]=j
        dict1.remove(j)
        break
print(s)        