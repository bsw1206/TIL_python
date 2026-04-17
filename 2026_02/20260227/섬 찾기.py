import sys
sys.stdin = open('섬 찾기.txt')
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(r, c):
    visited[r][c] = True
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < N and 0<= nc < M and island[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(r,c)

N, M = map(int, input().split())
island = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and not visited[i][j]:
            cnt += 1
            dfs(i,j)
print(cnt)