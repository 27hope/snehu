num=int(input())
lt=list(map(int,input().split()))[:num]
lt.sort()
print(*lt,end=" ")
