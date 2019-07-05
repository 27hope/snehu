num1,num2=map(int,input().split())
count=0
for i in range(num1,num2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
 
           

