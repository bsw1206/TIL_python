import sys
sys.stdin = open('swea_1251_하나로.txt')
from heapq import heappop, heappush

def prim(tax):

    q = [(0, 0)]

    
    visited = [0] * (N + 1)
    min_cost = 0

    while q:
        cost, node = heappop(q)

        if visited[node]:
            continue
        visited[node] = 1
        min_cost += cost
        for next_node in range(N):
            if visited[next_node]:
                continue

            next_cost =  (((x_lst[next_node] - x_lst[node]) ** 2) +  ((y_lst[next_node] - y_lst[node]) ** 2)) * tax

            heappush(q, (next_cost, next_node))
    return round(min_cost)

        

    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    min_val = prim(E)
    print(f'#{tc} {min_val}')