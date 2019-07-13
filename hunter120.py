num1=int(input())
count=0
lst=list(map(int,input().split()))[:num1]
for i in range(num1-1):
    for j in range(i+1,num1):
        for k in range(i+2,num1):
            if lst[i]+lst[j]==lst[k]:
                count+=1

print(count)
        
