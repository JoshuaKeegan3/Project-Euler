# Find the sum of all the positive integers
# which cannot be written as the sum of two abundant numbers.
# By mathematical analysis, it can be shown that all integers greater than 28123
# Can be expressed as the sum of two abundant numbers
# 12 is the smallest abundant number
# The samllest number that can be writen as the sum of two abudant numbers is 24

def abundant(num):
   return sum(i if num%i==0 else 0 for i in range(1,num))>num
      

abundant_numbers = []
max_value=28123
done=False
num=0
s =0
sum_of_twos=set()
while num<28123:
   while not abundant(num):
      s+=num
      num+=1
   abundant_numbers.append(num)
      

   for abundant_number in abundant_numbers:
      if num + abundant_number < 28123:
         sum_of_twos.add(num + abundant_number)

   num+=1

print(sum(i if i not in sum_of_twos else 0 for i in range(28123)))
