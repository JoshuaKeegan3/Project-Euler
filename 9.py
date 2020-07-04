# A pthagorean trplet is a set of three natural numbers, a < b < c for which,
# a^2 + b^2 = c^2
# For example 3^2+4^2 = 9+16 = 25= 5^2
# There exists exactly one pythagorean triplet for which a+b+c=1000
# Find the product abc

a=1
b=500
c=0

while a+b+c!=1000:
   b+=1
   if a+b+c>1000:
      a+=1
      b=1
   c = (a**2+b**2)**0.5
print(a*b*c)
