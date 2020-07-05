# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
total = 1
size = 1001
for i in range(3,size+1,2):
   minus = i-1
   current=i*i
   for j in range(4):
      total += current
      current -= minus
print(total)
   
