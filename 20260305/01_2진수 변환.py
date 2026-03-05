import sys
sys.stdin = open('input.txt')

num = str(input().strip())

results = []

for i in range(0, len(num), 7):
    group = num[i : i + 7]
    decimal_val = 0
    for j in group:
        decimal_val *=  2 
        decimal_val += int(j)
    results.append(decimal_val)

print(*results)