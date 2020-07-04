# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
day = 0
wd =0
month=0
year = 1901

sdays=0
months = [31,28,31,30,31,30,31,31,30,31,30,31]
if year%400==0:
   months[1]==29
elif year%100==0:
   months[1]==28
elif year%4==0:
   months[1]==29
else:
   months[1]==28
wd=0
while year<2000:
   day+=1
   wd+=1
   if wd%7==0:
      if day == 1:
         sdays+=1
         
      wd=0
   if day==months[month]:
      month+=1
      day=0
   if month==12:
      month=0
      year+=1
      
      if year%400==0:
         months[1]=29
      elif year%100==0:
         months[1]=28
      elif year%4==0:
         months[1]=29
      else:
         months[1]=28
print(sdays)
