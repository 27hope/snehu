num1=int(input())
lst=list(map(int,input().split()))
count=0

for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for k in range(j+1,len(lst)): 
 
            if lst[i]<lst[j] and lst[j]<lst[k]:
                count+=1
print(count)
