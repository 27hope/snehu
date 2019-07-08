from itertools import permutations
str1=list(input())
perm = permutations(str1)
for i in list(perm):
    print(*i,sep="")
