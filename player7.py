str1,str2=map(str,input().split())
for u in str1:
    p=str1.count(u)
for y in str2:
    q=str2.count(y)
if(p==q):
    print("yes")
else:
    print("no")
