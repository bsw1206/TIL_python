from heapq import heappop, heappush
import sys
input = sys.stdin.readline
tc = 1

def dijkstra():
    grid = [[float('inf')] * N for _ in range(N)]    
    pq = ([(cave[0][0], 0, 0)])
    grid[0][0] = cave[0][0]
    min_loss = 0

    while pq:
        
        cur_loss, r, c = heappop(pq)

        if cur_loss > grid[r][c]:
            continue

        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            
            if 0 <= nr < N and 0 <= nc < N:
                next_loss = cur_loss + cave[nr][nc]
                if next_loss < grid[nr][nc]:
                    grid[nr][nc] = next_loss
                    heappush(pq, (min_loss + next_loss, nr, nc))
    
    return grid[N - 1][N - 1]


while True: 
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'Problem {tc}: {dijkstra()}') 
    tc += 1