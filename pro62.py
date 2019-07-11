str1=input()
lst=[]
for i in range(0,len(str1)-1):
  for j in range(i+1,len(str1)):
    temp=str1[i:j+1]
    len1=temp[::-1]
    if temp==len1:
      lst.append(len(str1)-len(len1))
print(min(lst))
