str1=str(input())
count=0
for a in str1:
    if (a.isnumeric())==True:
        count+=1

if(count==len(str1)):
    print("yes")
else:
    print("no")
    
