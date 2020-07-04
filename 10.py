# Find the sum of all the primes below two million
primes = [2]
n=3
while n<2000000:
   for prime in primes:
      if n%prime==0:
         break
   else:
      primes.append(n)
   n+=1

print(sum(primes))
