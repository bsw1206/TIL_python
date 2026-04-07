# 먼저 섬의 정보를 저장
# 상하좌우로 움직이면서 서로 연결되어 있는지 파악, 연결 길이
# 그 연결 길이의 최솟값을 구하기
from collections import deque
from heapq import heappop, heappush
import sys
sys.stdin = open('boj_17472_다리 만들기 2.txt')


def bfs(start_r, start_c, num):
    
    
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    grid[start_r][start_c] = num
    while q:
        r, c = q.popleft()
        
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    grid[nr][nc] = num
                    q.append((nr, nc))
    
    


def check_connect(Grid):
    pass
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(N):
        for c in range(M):
            if Grid[r][c][0] != 0:
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    cnt = 0
                    while Grid[nr][nc][0] == 0 or  Grid[nr][nc][1] == Grid[r][c][1]:
                        nr += dr[i]
                        nc += dc[i]
                        cnt += 1
                        if not (0<= nr < N or 0<= nc < M):
                            continue
                    return [(Grid[r][c][1], Grid[nr][nc][1], cnt)]



N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
num = 1
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0 and not visited[i][j]:            
            bfs(i, j, num)
            num += 1

edges = set()
for r in range(N):
    for c in range(M):
        if grid[r][c] > 0:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                dist = 0
                while 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] == grid[r][c]:
                        break
                    if grid[nr][nc] > 0:
                        if dist >= 2:
                            edges.add((dist, grid[r][c], grid[nr][nc]))
                        break
                    
                    dist += 1
                    nr += dr
                    nc += dc

edges = sorted(list(edges))
parents = [i for i in range(num)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
total_cost = 0
cnt = 0

for dist, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        total_cost += dist
        cnt += 1
if cnt == (num - 1) - 1:
    print(total_cost)
else:
    print(-1)
