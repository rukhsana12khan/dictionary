
dic=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
d=[]
for i in dic:
    s={}
    for j in i:
        k=int(i[j])
        s[j]=k
    d.append(s)
print(d)        





# dic=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# s=[]
# for i in dic:
#     d={}
#     for j in i:
#         g=float(i[j])
#         d[j]=g
#     s.append(d)
# print(s)        
