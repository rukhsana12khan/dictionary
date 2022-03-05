dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# print ("{:<1} {:<1} {:<1}".format('c1', 'c2','c3'))
# for key, value in dic.items():
#     c1,c2,c3 = value
#     print ("{:<1} {:<1} {:<1}".format(c1, c2, c3))


print(*list(dic.keys()))
a=list(dic.values())
for i in range(len(a)):
    print(*a([i]))

