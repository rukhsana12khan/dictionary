dic={'kiran': 10, 'ramesh': 20, 'rajita': 30, 'rakesh': 40, 'rani': 50, 'moni': 60}
first=0
max=0
smax=0
tmax=0
scond=0
thrd=0
for i in dic.keys():
    if dic[i]>first:
        scond=tmax
        tmax=first
        first=dic[i]
        max=i
    if dic[i]!=first and dic[i]>scond:
        tmax=first
        first=scond
        tmax=max
        max=smax
        smax=i
        scond=dic[i]
print(max,first)   
print(smax,scond) 