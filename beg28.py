num1=int(input())
lst=list(map(int,input().split()))[:num1]
for i in range (0,num1):
    print(lst[i],i)
