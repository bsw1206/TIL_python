import sys
sys.stdin = open('swea_5249_최소 신장 트리.txt')
from heapq import heappop, heappush

def prim(start_node):

    q = []
    heappush(q, (0, start_node))
    sum_val = 0
    cnt = 0
    while q:
        weight, node = heappop(q)

        if visited[node]:
            continue

        visited[node]= True
        sum_val += weight
        cnt += 1

        for next_weight, next_node in adj_lst[node]:
            if visited[next_node]:
                continue
            else:
                heappush(q, (next_weight, next_node))
    return sum_val


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_lst[n1].append((w, n2))
        adj_lst[n2].append((w, n1))
    visited = [False] * (V + 1)

    result = prim(0)
    print(result)