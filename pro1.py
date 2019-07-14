import os
num1=int(input())
lst=[]
for i in range(num1):
    lst.append(input())
print(os.path.commonprefix(lst))
