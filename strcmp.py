str1,str2=map(str,input().split())
count=0
for x in range(len(str1)):
    if str1[x]!=str2[x]:
        count+=1

if(count==1):
    print("yes")
else:
    print("no")

    
