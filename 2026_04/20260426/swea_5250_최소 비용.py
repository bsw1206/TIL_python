# 4방향 도는 것을 좀 다르게 표현 해봤습니다.
from heapq import heappop, heappush
# import sys
# sys.stdin = open('swea_5250_최소 비용.txt')

def dijkstra():
    dist = [[float('inf')] * N for _ in range(N)]


    dist[0][0] = 0 # 맨 처음 값은 0
    
    pq = ([(0, 0, 0)]) # 현재 비용, row, col순으로 저장

    while pq:
        value, r, c = heappop(pq) # value의 최소인 경우를 pop
        
        if value > dist[r][c]: # 이미 저장된 값보다 더 큰 경우(가지치기)
            continue

				# 튜플 형식의 방향을 순회
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):


            if 0<= nr < N and 0 <= nc < N:
                diff = 1 # 기본 값이 1
                
								# 더 높은 곳을 갈 때
                if grid[nr][nc] > grid[r][c]:
                    diff += grid[nr][nc] - grid[r][c]
                next_diff = value + diff
                
                # 더 적은 비용으로 갈 수 있을 때
                if next_diff < dist[nr][nc]:
                    dist[nr][nc] = next_diff

                    heappush(pq, (next_diff, nr, nc))
    
    
    return dist[N-1][N-1] # 도착점의 비용 반환(최소)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    

    print(f'#{tc} {dijkstra()}')