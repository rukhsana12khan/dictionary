list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
m={}
for i in list1:
    for j in list2:
        m[i]=j
        list2.remove(j)
        break
print(m)    