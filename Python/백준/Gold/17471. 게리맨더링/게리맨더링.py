from itertools import combinations
from collections import deque


def check_group(group):
    if not group:
        return False
    q = deque([group[0]])
    visited = set([group[0]])
    count = 1

    while q:
        node = q.popleft()
        for neighbor in arr[node]:
            if neighbor in group and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                count += 1
    if count == len(group):
        return True 


N = int(input())
arr = [[] for _ in range(N + 1)]
p_lst = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    n_lst = list(map(int, input().split()))
    for j in range(1, len(n_lst)):
        arr[i].append(n_lst[j])
min_val = float('inf')

num = list(range(1, N + 1))
for a in range(1, N + 1):
    for b in combinations(num, a):
        b = list(b)
        d = [x for x in num if x not in b]
   
        if check_group(b) and check_group(d):
            b_sum, d_sum = 0, 0
            for i in b:
                b_sum += p_lst[i]
            for j in d:
                d_sum += p_lst[j]
            sub_val = abs(d_sum - b_sum)
            min_val = min(min_val, sub_val)
if min_val == float('inf'):
    print(-1)
else:
    print(min_val)