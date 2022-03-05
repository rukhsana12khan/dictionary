# # d={"fantasy": "harrypotter","romance": "me before you","fiction": "divergent"}
# # print(d.items())
# # print(d.iteritems())


# # dict ={}
 
# # # Insert data into dictionary
# # dict1 = {1: ["Samuel", 21, 'Data Structures'],
# #      2: ["Richie", 20, 'Machine Learning'],
# #      3: ["Lauren", 21, 'OOPS with java'],
# #      }
 
# # # Print the names of the columns.
# # print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
 
# # # print each data item.
# # for key, value in dict1.items():
# #     name, age, course = value
# #     print ("{:<10} {:<10} {:<10}".format(name, age, course))








# # dictA = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3}

# # print("Given Dictionary :", dictA)

# # k= {}

# # for x, y in dictA.items():
# #    if y not in k:
# #       k[y] = [x]
# #    else:
# #       k[y].append(x)

# # # Result
# # print("New Dictionary:", k)
# dict = {'data1':100,'data2': -54,'data3': 247}
# sum=0
# for i in dict.values():
#    sum=sum+i
# print(sum)   

# list1=[“one”,”two”,”three”,”four”,”five”]
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# s={}
# for i in list1:
#    for j in list2:
#       if i==j:
#          s[i]+=1
#       else:
#          s[i]=1
# print(s)
#             
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# dic.update()
# print(dic)


# s=[dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}
# ]]
# for i in dic:
#    for j in i.values():
#       if j not in s:
#          s.append(j)
# print(s)

# s={}
# i=0
# while i<=10:
#    a=input("enter a name")
#    b=int(input("enter a number"))
#    s[a]=b
#    print(s)
#    i+=1


# dic="MISSISSIPPI"
# s={}
# for i in dic:
#    if i in s:
#       s[i]+=1
#    else:
#       s[i]=1
# print(s)           

# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
# sum=0
# for i in dict1.values():
#    for j in i: 
#       sum+=1
# # print(sum)   

#from distutils.errors import DistutilsClassError


# dic= {'a':50,'b':58,'c':56,'d':40,'e':100, 'f':20}
# max=0
# smax=0
# tmax=0
# m=0
# s=0
# t=0
# s=[]
# for i in dic:
#     if dic[i]>max:
#         tmax=smax
#         t=s
#         smax=max
#         s=m
#         max=dic[i]
#         m=i
#     if dic[i]!=max and dic[i]>smax:
#         tmax=smax
#         t=s
#         smax=dic[i]
#         s=i
#     if dic[i]!=max and dic[i]!=smax and dic[i]>tmax:
#         tmax=dic[i]
#         t=i          
# print(m,s,t)    


# s={}
# i=0
# while i<=15:
#     s[i]=i*i
#     i+=1 
# print(s)     


#   docs questints

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)            
    
# a='w3resource'
# s={}
# for i in a:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1    
# print(s)    

# s={}
# a=int(input('enter'))
# for i in range(1,a):
#     s[i]=i*i
# print(s)

# s={}
# for i in range(1,16):
#     s[i]=i*i
# print(s)    

# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s=[]
# for x in dic.items():
#     s.append(x)
#     s.sort()
# print(s)

# dic={0: 10, 1: 20}
# dic[2]=30
# print(dic)


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# s={}
# for i in dic1:
#     for j in dic2:
#         if i==j:
#             s[i]=dic1[i]+dic2[j]
#         else:
#             s.update(dic1)
#             s.update(dic2)
#             s.update(dic3) 
# print(s)            

# dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# sum=0
# key=0
# for i in dic:
#     sum=sum+dic[i]
#     key+=i
# print(sum)    
# print(key)

# dic=[1,3,9,0,8]
# dic1=['rupa','rajita','rakesh','runu','raam']
# s={}
# for i in dic:
#     for j in dic1:
#         s[i]=j
#         dic1.remove(j)
#         break
# print(s)        

# dic={1:6,3:9,9:6,0:2,8:8}
# s={}
# for  i in sorted(dic):
#     s[i]=dic[i]
# print(s)


# dic={'j':6,'f':7,'c':6,'b':2,'a':8}
# max=0
# min=0
# for i in dic:
#     if dic[i]>max:
#         max=dic[i]
#     else:
#         dic[i]<min
#         min=dic[i]    
# print(i,max)
# print(min)        



# dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# s=[]
# for i in dic:
#     for j in i.values():
#         if j not in s:
#             s.append(j)
# print(set(s))            


# dic={'1':['a','b'], '2':['c','d']}
# i,j=dic.values()
# for a in i:
#     for k in j:
#         print(a,k)

# e={"a":[2,3,7,10],"b":[4,1],"c":[3,9,6]}
# d={}
# for i,j in e.items():
#     s=[]
#     for k in j:
#         if k%2==0:
#             s.append(k)
#             e[i]=s
#     d[i]=s       
# print(d)


# dic="ayushiparmar"
# s={}
# for i in dic:
#     if i  in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(s)

# dic= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print("{:<1} {:<1} {:<1}".format('c1','c2','c3'))
# for i,j in dic.items():
#     c1,c2,c3=j
#     print("{:<1} {:<1} {:<1}".format(c1,c2,c3))

# dic=[1,2,3,4]
# s={}
# a=s
# for i in dic:
#     s[i]={}
#     s=s[i]
# print(a)    

# dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# s={}
# for i,j  in dic.items():
#     for  k in " ":
#         i=i.replace(k,'')
#         s[i]=j
# print(s)        


# dic={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=0
# smax=0
# tmax=0
# m=0
# s=0
# t=0
# for i in dic:
#     if dic[i]>max:
#         tmax=smax
#         t=s
#         smax=max
#         s=m
#         max=dic[i]
#         m=i
#     if dic[i]!=max and dic[i]>smax:
#         tmax=max
#         t=m 
#         smax=dic[i]
#         s=i
#     if dic[i]!=max and dic[i]!=smax and dic[i]>tmax:
#         tmax=dic[i]
#         t=i
# print(m,s,t)        



# dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# print("{:<1} {:<1} {:<1}".format("key","value","count"))
# for i ,j in dic.items():
#     count=count+1
#     print("{:<1} {:<1}  {:<1}".format(i,j,count))

# st= {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}  
# for i in st:
#     print(i)
#     for j in st[i]:
#         print(j,":",st[i][j])

    
# dic={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sum=0
# for i in dic:
#     for j in dic[i]:
#             sum=sum+1
# print(sum)        

                 
# dic={'key1': 1, 'key2': 3, 'key3': 2}
# dic1={'key1': 1, 'key2': 2}
# for i in dic:
#     for j in dic1:
#         if i==j and dic[i]==dic1[j]:
#             print(j,":",dic[i])


# a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in a:
#     for j in i:
#         print(a[i][4])

# dix={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dix.pop('c3')
# print(dix)


# dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# s={}
# for i ,j in dic.items():
#     if j>170:
#         s[i]=j
# print(s)        


# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# s=[]
# for i in a:
#     d={}
#     for j in b:
#         f={}
#         for k in c:
#             f[j]=k
#             d[i]=f
#             s.append(d)
#             c.remove(k)
#             break
#         b.remove(j)
#         break
# print(s)    


# dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# s={}
# for i ,j in dic.items():
#     if j[0]>=6.0 and j[1]>=70:
#         s[i]=j
# print(s)        


# dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# num=int(input('enter'))
# for i ,j in dic.items():
#     if j==num:
#         print('true')
#         break
#     else:
#         print("false") 
#         break   

# dic=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# y=[]
# b=[]
# r=[]
# s={}
# for i,j in dic:
#     if i=="yellow":
#         y.append(j)
#         s[i]=y
#     if i=="blue":
#         b.append(j)
#         s[i]=b
#     if i=="red":
#         r.append(j)
#         s[i]=r
# print(s)                          


# dic=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
#  {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# s=[]
# for i in dic:
#     if (i['id'])!='#FF0000':
#         s.append(i)   
# print(s)        

#from socket import J1939_NLA_BYTES_ACKED


# dic=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# d=[]
# for i in dic:
#     s={}
#     for j in i:
#         k=int(i[j])
#         s[j]=k
#     d.append(s)
# print(d)        

# dic=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# s=[]
# for i in dic:
#     d={}
#     for j in i:
#         g=float(i[j])
#         d[j]=g
#     s.append(d)
# # print(s)        


# dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i,j in dic.items():
#     d=[]
#     for k in j:
#         if k%2==0:
#             d.append(k)
#             dic[i]=d 
# print(dic)            



s="ilovechocalate"
w={}
count=0
for i  in s:
    if i not  in w:
            count+=1 
            # d.append(i)
            # d.append(count)
    w[i]=count 
print(w)


# dic={"R 007":["rajitha","rani"],"k 789":["ramya","shanti"]}
# s={}
# for i,j in dic.items():
#         for k in " ":
#             i=i.replace(k,"")
#             s[i]=j 
# print(s)            








