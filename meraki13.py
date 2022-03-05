dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
max=0
smax=0
tmax=0
fmax=0
s=0
t=0
s=[]
for i in dict:
    if dict[i]>max:
        tmax=smax
        smax=max
        max=dict[i]
    if smax<dict[i] and dict[i]<max:
        smax=dict[i]     
print(max)
print(smax)        
print(tmax)