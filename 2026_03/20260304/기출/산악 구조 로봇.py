# 로봇의 출발지 (1, 1) -> (0, 0)

# 조난자의 위치 (N, N) -> (N-1, N-1)

# 로봇이 상, 하, 좌, 우로 이동
# 높이 같을 때? 연료 1소모 / 높이 낮을 때? 연료 소모 x / 높이 높을 때? 높이 차의 두배만큼 연료 소모

# 최소 연료 소비하는 경우의 수

# bfs 함수를 정의해서 소비되는 연료의 수를 정의하고 queue에서 뽑은 것을 원래의 연료 소비와 비교하여 
# 더 작은 값을 queue에 추가함.
# 4방향 돌고 벽 부딪히는 여부 파악
# 같은 경우, 낮은 경우, 높은 경우 파악하고
import sys
sys.stdin = open('산악 구조 로봇.txt')
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(start_r, start_c):
    distance = [[float('inf')] * N for _ in range(N)]
    distance[start_r][start_c] = 0
    q = deque([(start_r, start_c)])
    
    while q:
        r, c, = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr < N and 0<= nc < N:
                if ground[nr][nc] > ground[r][c]:
                    cost = (ground[nr][nc] - ground[r][c]) * 2
                    
                elif ground[nr][nc] == ground[r][c]:
                    cost = 1
                else:
                    cost = 0
                cur_gas = distance[r][c] + cost
                if cur_gas < distance[nr][nc]:
                    distance[nr][nc] = cur_gas
                    q.append((nr,nc))
    return distance[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(0, 0)}')