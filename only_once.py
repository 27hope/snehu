num1=int(input())
s=input().split()[:num1]
for i in s:
    if s.count(i)==1:
        print(i)
        break
    
