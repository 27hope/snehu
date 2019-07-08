n,k=map(int,input().split())


lt=list(map(int,input().split()))[:n]
lt.sort(reverse=True)
print(lt[k-1])
