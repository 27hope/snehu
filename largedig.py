num=int(input())
s=list(map(int,input().split()))[:num]
s.sort(reverse=True)
print(*s,sep="")
