num1=int(input())
lst=list(map(int,input().split())) [:num1]
lt=[]
for i in range (0,num1):
  lt.append(lst[i])
  lt.sort()
  print(lt[0],end=" ")
