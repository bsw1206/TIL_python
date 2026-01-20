a, b = map(int, input().split())
dividing_list = []
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        dividing_list.append(i)
max_val = max(dividing_list)
print(max_val)
print(int(a * b / max_val))