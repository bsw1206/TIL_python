import sys
import heapq
sys.stdin = open('swea_5249_최소 신장 트리.txt')
def dijkstra(start_node):
    heap = ([(0, start_node)])
    sum_val = 0
    cnt = 0

    while heap and cnt < V + 1:
        weight, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        sum_val += weight
        cnt += 1


        for next_weight, next_node in adj_lst[node]:
            if visited[next_node]:
                continue
            else:
                heapq.heappush(heap, (next_weight, next_node))
    return sum_val



T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V + 1)]
    for _ in range(E):
        p1, p2, weight = map(int, input().split())
        adj_lst[p1].append((weight, p2))
        adj_lst[p2].append((weight, p1))
    
    visited = [False] * (V + 1)

    print(f'#{tc} {dijkstra(0)}')

    