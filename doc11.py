dic1={
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
dic2={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
c={}
for i in (dic1,dic2):
    c.update(i)
print(c)    

