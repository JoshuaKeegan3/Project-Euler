# Which starting number, under one million, produces the longest colatz squence?

def collatz_chain_length(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x / 2
	else:
		y = x * 3 + 1
	return collatz_chain_length(y) + 1
m=0
mc=0
for x in range(1, 1000000):
   c=collatz_chain_length(x)
   if c>mc:
      m=x
      mc=c
print(m)
