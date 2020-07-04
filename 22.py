def alphabetical_value(name):
   return sum(ord(letter.lower())-96 for letter in name)

def execute(names):
   tot=0
   names=names.replace('"',"")
   names=names.split(",")
   for i, name in enumerate(sorted(names)):
      tot+=alphabetical_value(name)*(i+1)
   print(tot)
file = open("22.txt")
execute(file.read())
file.close()
