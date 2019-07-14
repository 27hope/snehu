str1=str(input())
lst=""
rev=str1
flag=0
for i in range(1,len(str1)):
    lst=str1[i:]
    if(lst[0]>str1[0]):
        rev=lst
        f=1
        break
print(rev) 
