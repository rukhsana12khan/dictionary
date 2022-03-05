dic1={'key1': 1, 'key2': 3, 'key3': 2}
dic2={'key1': 1, 'key2': 2}
dic={}
for i in dic1:
    for j in dic2:
        if i==j and dic1[i]==dic2[j]:
            dic[i]=dic1[i]
            print(i,':',dic1[i])



       
# dic={'key1': 1, 'key2': 3, 'key3': 2}
# dic1={'key1': 1, 'key2': 2}
# for i in dic:
#     for j in dic1:
#         if i==j and dic[i]==dic1[j]:
#             print(j,":",dic[i])

