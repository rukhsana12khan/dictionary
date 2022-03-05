dict = {'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
s=[]
fmax=0
smax=0
tmax=0
for i in dict:
    if dict[i]>fmax:
        tmax=smax
        smax=fmax
        fmax=dict[i]
    if smax<dict[i]and dict[i]<fmax:
        smax=dict[i]
s.append(fmax)    
s.append(smax)
s.append(tmax)    
print(s)  
