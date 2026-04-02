T = int(input())
number = str(input())
sum = 0
for i in range(1, T + 1):
	sum += int(number[i-1])
print(sum)