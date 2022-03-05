dict = {'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
max=0
min=0
for i in dict:
    if dict[i]>max:
        max=dict[i]
    else:
         dict[i]<min
         min=dict[i]
print("minimmum",min)
print("maximum",max)