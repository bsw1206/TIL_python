
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    distance = [[0] * N for _ in range(N)]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr < N and 0 <= nc < N and not distance[nr][nc]:
                if maze[nr][nc] == 3:
                    return distance[r][c] 
                elif maze[nr][nc] == 0:
                    distance[nr][nc] = distance[r][c] + 1
                    q.append((nr, nc))   
    return 0  

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c
                break
    print(f'#{tc} {bfs(start_r, start_c)}')
