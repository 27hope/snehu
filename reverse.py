def reverse(str1):
    s=str1[::-1]
    return s
str1=str(input())
if len(str1)<=1000:
    
    print(reverse(str1))

else:
    print("invalid")
