from heapq import heappop, heappush

import sys
sys.stdin = open('swea_1249_보급로.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    

    dists = [[float('inf')] * N for _ in range(N)]

    pq = [(0, 0, 0)]
    dists[0][0] = 0
    
    while pq:
        dist, r, c = heappop(pq)

        

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                
                new_dist = dist + MAP[nr][nc]

                if new_dist < dists[nr][nc]:
                    dists[nr][nc] = new_dist 
                    heappush(pq, (new_dist, nr, nc))

    return dists[N-1][N-1]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().strip())) for _ in range(N)]

    min_val = dijkstra()
    print(f'#{tc} {min_val}')