import sys
sys.stdin = open('swea_1226_미로1.txt')
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c):

    q = deque([(start_r, start_c)])
    
    visited[start_r][start_c] = True

    while q:

        r, c = q.popleft()

        for i in range(4):
            
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                
                if maze[nr][nc] == 3:
                    return 1
                
                if maze[nr][nc] == 0:

                    visited[nr][nc] = True
                    q.append((nr, nc))
        
    return 0



for _ in range(1, 11):

    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    visited = [[False] * N for _ in range(N)]            

    print(f'#{tc} {bfs(1, 1)}')