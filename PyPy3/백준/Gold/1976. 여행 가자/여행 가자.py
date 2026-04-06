

import sys
input = sys.stdin.readline

def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):

    ref_x = find_set(parent, x)
    ref_y = find_set(parent, y)

    if ref_x == ref_y:
        return
    
    if rank[ref_x] > rank[ref_y]:
        parent[ref_y] = ref_x
    elif rank[ref_y] > rank[ref_x]:
        parent[ref_x] = ref_y
    else:
        parent[ref_x] = ref_y
        rank[ref_y] += 1

N = int(input())
M = int(input())

adj_lst = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))


parent = list(range(N + 1))
rank = [0] * (N + 1)


for i in range(N):
    for j in range(N):
        if adj_lst[i][j] == 1:
            union(parent, rank, i + 1, j + 1)

check = find_set(parent, plan[0])
result = 'YES'

for i in range(1, len(plan)):
    if check != find_set(parent, plan[i]):
        result = 'NO'
        break
print(result)
