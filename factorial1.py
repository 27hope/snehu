num1=int(input())
fact=1
if num1<0:
    print("no factorial for negative number")
elif num1==0:
    print("1")
else:
    for i in range(1,num1+1):
        fact=fact*i
    print(fact)
    
