import sys
sys.stdin = open('swea_1226_미로1.txt')
from collections import deque
################################################################

# BFS
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True # 시작 위치 방문처리
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i] # 4방향 이동
            # 벽 충돌 여부, 방문 여부 파악
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and visited[nr][nc] != 1:
                if maze[nr][nc] == 3: # 도착점 발견!
                    return 1
                if maze[nr][nc] == 0: # 길 발견!
                    visited[nr][nc] = True # 방문 처리
                    q.append((nr, nc)) # queue에 경로 추가
    return 0 # 못 찾으면 0 출력

for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    
    visited = [[False] * 16 for _ in range(16)]
    # start_r, start_c = 1, 1
    result = bfs(1, 1) # 시작 위치 (1,1)로 정했으므로 굳이 따로 정할 필요 x
    print(f'#{T} {result}')

###########################################################
# DFS(재귀)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if maze[r][c] == 3: # 도착점 찾았을 때는 바로 True 반환
        return True
    visited[r][c] = True # 방문 처리
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i] # 4방향 탐색
        # 벽 충돌 여부, 방문 여부 파악
        if 0<= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1 and not visited[nr][nc]:
            if dfs(nr, nc): # 도착점을 찾아서 True가 반환됬을 때
                return 1
            
    return 0 # 4방향을 돌아도 못 찾았으면 종료
    

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    result = dfs(1, 1)
    print(f'#{tc} {result}')
    
