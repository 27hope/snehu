n=int(input())
s=list(map(int,input().split()))[:n]
m=[]
for i in range(len(s)):
    k=i+1
    for j in range(k,len(s)) :
        
        if(s[i]==s[j] and s[i] not in m):
            m.append(s[i])
m.sort()
if(m):
    for i in m:
        print(i,end=" ")
else:
    print("unique")
