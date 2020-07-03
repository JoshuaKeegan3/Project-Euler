#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
num=6000851475143
ans=1
for i in range (2, num // 2): # There can't be anything more than this
    if num==1:
        break
    if num % i == 0:
        for x in range(2, i+1):
            if i==x:
                while num % i == 0:
                    num /= i
                ans=i
                print(ans,num)
            else:
                if i%x==0:break
print(ans)
