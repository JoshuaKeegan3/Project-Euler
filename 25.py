# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?
fib=1
next_fib=0
prev_fib=1
count=2
while len(str(fib))<1000:
   count+=1
   next_fib=prev_fib+fib
   prev_fib=fib
   fib=next_fib
   
print(count)
