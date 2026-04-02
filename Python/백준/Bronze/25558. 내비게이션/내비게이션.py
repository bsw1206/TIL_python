import sys

N = int(input())
sx, sy, ex, ey = map(int, input().split())

min_val = float('inf')
sum_lst = []
for i in range(1, N + 1):
    sum_val = 0
    cur_x, cur_y = sx, sy
    M = int(input())
    for _ in range(M):
        x, y = map(int, input().split())
        sum_val += abs(x - cur_x) + abs(y - cur_y)
        cur_x, cur_y = x, y
    sum_val += (abs(ex - cur_x) + abs(ey - cur_y))
    sum_lst.append((sum_val, i))
result = 1
for val, idx in sum_lst:
    if min_val > val:
        min_val = val
        result = idx
print(result)