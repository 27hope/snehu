num1 = int(input())
dia = 0
m = [ [int(i) for i in input().split()] for j in range(num1)]
for j in range(num1):
	dia += m[j][(num1-1)-j]
print(dia)
