import heapq

def dijkstra(start_node, V):

    distance = [float('inf')] * (V + 1)

    q = ([(0, start_node)])

    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for weight, next_node in adj_lst[node]:
            next_dist = dist + weight

            if next_dist < distance[next_node]:

                distance[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))

    return distance




T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj_lst = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_lst[s].append((w, e))
        
    

    result = dijkstra(0, N)
    
    print(f'#{tc} {result[N]}')