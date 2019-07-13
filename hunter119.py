num1=int(input())
count=0
lst=list(map(int,input().split()))[:num1]
for i in range(0,num1):
    for j in range(i+1,num1):
        if lst[i]<lst[j] and i<j:
            count+=1
print(count)
