import sys
sys.stdin = open('산악 구조 로봇.txt')
from heapq import heappop, heappush
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dijkstra():
    
    dist = [[float('inf')] * N for _ in range(N)]

    dist[0][0] = 0
    # 최소 비용, row, col
    q = [(0, 0, 0)]
    while q:
        c_cost, r, c = heappop(q)

        if c_cost > dist[r][c]:
            continue
        if r == N - 1 and c == N - 1:
            return c_cost
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            

            if 0<= nr < N and 0<= nc < N:
                fuel = 0
                diff = grid[nr][nc] - grid[r][c]
                if grid[nr][nc] > grid[r][c]:
                    fuel = diff * 2
                elif grid[nr][nc] == grid[r][c]:
                    fuel = 1
                new_cost = c_cost + fuel
                if dist[nr][nc] > new_cost:
                    dist[nr][nc] = new_cost
                    heappush(q, (new_cost, nr, nc))
    return dist[N-1][N-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {dijkstra()}')