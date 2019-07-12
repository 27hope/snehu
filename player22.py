n,k=map(int,input().split())
lst=[]
if n > k:
  small = k
else: 
  small = n 
for i in range(1, small+1): 
  if((n % i == 0) and (k % i == 0)):
    lst.append(i)
lst.sort()

print(lst[-1])
