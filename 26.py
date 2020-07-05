# 1/? gives most repeating decimal places
import decimal
g=0
decimal.getcontext().prec = 10000
v=0
for d in range(2,1000):
   n = decimal.Decimal(1)/decimal.Decimal(d)
   s = str(n)
   l=[]
   for c in reversed(s):
      l.append(c)
      if l[:len(l)//2]==l[len(l)//2:]:
         if g<len(l)//2:
            g=len(l)//2
            v=d
         break
   
print(v)
