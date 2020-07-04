# Evaluate the sum of all the amicable numbers under 10000
def d(n):
   return sum(x if n%x==0 else 0 for x in range(1,n//2+1))
s=0
for a in range(10000):
   b=d(a)
   if d(b)==a and a!=b:
      s+=a
print(s)
