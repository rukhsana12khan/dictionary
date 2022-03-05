num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count=0
print("{:<1} {:<1} {:<1}".format('key','values','count'))
for i, j in num.items():
    count=count+1
    print("{:<1} {:<1} {:<1}".format(i,j,count))
