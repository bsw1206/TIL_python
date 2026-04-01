import sys
input = sys.stdin.readline
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, remain_pattern_usage, visited_2):
    if MAP[start_r][start_c] == 2:
        visited_2 = 1
    
    q = deque([(start_r, start_c, remain_pattern_usage, visited_2, 0)])
    visited[start_r][start_c][remain_pattern_usage][visited_2] = True

    while q:
        r, c, pattern_usage, has_2, dist = q.popleft()

        if r == N - 1 and c == M - 1 and has_2 == 1:
            return dist
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0<= nr < N and 0<= nc < M and MAP[nr][nc] != 1:
                if has_2 == 1 or MAP[nr][nc] == 2:
                    n_has_2 = 1
                else:
                    n_has_2 = 0
                if not visited[nr][nc][pattern_usage][n_has_2]:   
                    visited[nr][nc][pattern_usage][n_has_2] = True
                    q.append((nr, nc, pattern_usage, n_has_2, dist + 1))
        
        if pattern_usage > 0:
            for tr, tc in pattern_moves:
                nr, nc = r + tr, c + tc
                if 0<= nr < N and 0 <= nc < M and MAP[nr][nc] != 1:
                    if has_2 == 1 or MAP[nr][nc] == 2:
                        n_has_2 = 1
                    else:
                        n_has_2 = 0
                    if not visited[nr][nc][pattern_usage - 1][n_has_2]:
                        visited[nr][nc][pattern_usage - 1][n_has_2] = True
                        q.append((nr, nc, pattern_usage-1, n_has_2, dist + 1))

    return -1

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
pattern = [list(map(int, input().split())) for _ in range(5)]
pattern_moves = []
for i in range(5):
    for j in range(5):
        if pattern[i][j] == 1:
            pattern_moves.append((i - 2, j - 2))
visited = [[[[False] * 2 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, K, 0))