s=int(input())
sum1=0
while(s!=0):
    num=s%10
    sum1=sum1+num*num
    s=s//10
print(sum1)
