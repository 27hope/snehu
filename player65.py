n,k=map(int,input().split())
li=list(map(int,input().split()))[:n]
cost=int(input())
pcost=(sum(li)-li[k])//2
if (cost==pcost):
    print("Bon Appetit")
else:
    print(abs(cost-pcost))
