# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
sumnum = 0
for i in range (0,1000,3):
    sumnum += i
for i in range (0,1000,5):
    sumnum += i
for i in range(0,1000,15):#take off the multiples of both that were added twice
    sumnum -= i
print(sumnum)
