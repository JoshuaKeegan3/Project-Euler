# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# how many letters would be used?
# the answer is actually 100 less and I have no idea why
ones = ["","one","two","three","four","five","six","seven","eight","nine"]
tenone = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

amount=0
mass_string=""
s=""
for h in range(10):
   if h>0:
      s=ones[h]+"hundred"
   for t in range(10):
      for o in range(10):
         if t == 1:
            amount+=len(s+tenone[o]+("and" if (t>0 or o>0) and h>0 else ""))
            mass_string+=s+tenone[o]+("and" if (t>0 or o>0) and h>0  else "")
         else:
            amount+=len(s+tens[t]+ones[o]+("and" if (t>0 or o>0) and h>0  else ""))
            mass_string+=s+tens[t]+ones[o]+("and" if (t>0 or o>0) and h>0  else "")

print(amount+len("onethousand"))
         
