n,k=map(int,input().split())
lst1=list(map(int,input().split()))[:n]
lst2=list(map(int,input().split()))[:k]
for i in range(len(lst2)):
    lst1.append(lst2[i])
    lst1.sort()
    print(lst1[-1],end=" ")
