tot=0
for i in range(2,1000001):
   tot += i if sum(int(v)**5 for v in str(i))==i else 0
print(tot)
   
