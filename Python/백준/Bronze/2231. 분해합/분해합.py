N = int(input())
result = 0
for i in range(1, N + 1):
    div_sum = i + sum(map(int, str(i)))
    if div_sum == N:
        result = i
        break
print(result)