# Find the 1,000,000th lexicographic permutation of the integer set 0-9
n = 0
i = 0
numbers = set([i for i in range(10)])
numbers2 = set([i for i in range(1,10)])
while n< 1000000:
   if all((str(num) in str(i) for num in numbers)) or all((str(num2) in str(i) and len(str(i)) < len(numbers) for num2 in numbers2)):
      n+=1
   i +=1
   
print(n-1)
