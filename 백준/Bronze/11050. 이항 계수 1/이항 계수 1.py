a, b = map(int, input().split())
result = 1
for i in range(1, a + 1):
	result = result * i
for j in range(1, b + 1):
	result = result // j
for k in range(1, a - b + 1):
	result = result // k
print(result)