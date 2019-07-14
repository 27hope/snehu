from itertools import permutations
n,k=map(int,input().split())
lst=list(map(int,input().split()))
for i in permutations(lst,2):
  if(sum(i)==k):
    print("yes")
    break
else:
    print("no")
