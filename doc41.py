dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 
'Pierre Cox': (5.8, 66)}
s={}
for i,j in dic.items():
    if j[0]>=6.0 and j[1]>=70: 
        s[i]=j
print(s)              
