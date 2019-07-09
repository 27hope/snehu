num1=int(input())
l=[]
lst=[]
for i in range(0,num1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)


for i in lst:
    for j in lst:
        for k in lst:
            f=i+j+k
            if f==num1:
                l.append([i,j,k])
print(*l[0])
        
        
