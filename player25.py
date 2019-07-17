import statistics
num1=int(input())
str1=list(map(int,input().split()))[:num1]
print(statistics.median(str1))
