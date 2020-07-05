# n2+an+b , where |a|<1000 and |b|≤1000
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with  n=0
m=0
primes=[2]
for a in range(-1000,1000):
   for b in range(1,1000):
      n =0
      v=0
      cv=True
      count=0
      while cv:
         v= n*n+a*n+b
         if v>primes[-1]:
            for i in range(primes[-1],v+1):
               for prime in primes:
                  if i%prime==0:
                     if i==v:
                        cv=False
                     break
               else:
                  if i==v:
                     count+=1
                  primes.append(i)
         elif v in primes:
            count+=1
         else:
            cv=False

         n+=1
                  
               
      if count>m:
         m=count
         p=a*b
            
print(p)
