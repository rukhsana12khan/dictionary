dic=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], 
[4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
i=0
s={}
while i<len(dic):
    j=0
    duc=0
    d=[]
    while j<len(dic[i]):
        if j==0:
            duc=dic[i][j]
        else:
            d.append(dic[i][j]) 
        j=j+1
    s[duc]=d
    i=i+1
print(s)               
