# 세로 N, 가로 M, 사용 횟수 K
# 0이 빈칸, 1이 벽, 2가 중간 거점지, 벽인 곳으로는 이동할 수 없음.
# N * M인 지도, 그 다음에 5 * 5 크기의 패턴 배열
# 3행 3열(한가운데)에는 모빌리티가 위치해 있음.
# 왼쪽 최상단에서 중간 거점지들 중에 최소 하나를 거쳐서 오른쪽 최하단으로 고정된 최종 목적지까지 가는 최단거리

# 일반적인 bfs도 포함하고, 도착 지점에 다다르면 

import sys
# sys.stdin = open('boj_25969_현대 모비스 자율 주행 시스템.txt')
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
        # has_2를 사용한 상태로 도달했니?
        if r == N - 1 and c == M - 1 and has_2 == 1:
            return dist
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 안에 있고 벽을 박지 않았을 때,
            if 0<= nr < N and 0<= nc < M and MAP[nr][nc] != 1:
                # 2를 방문했는지 확인하고 중간 지점을 만났을 때,
                if has_2 == 1 or MAP[nr][nc] == 2:
                    # 중간 지점을 거쳤다고 갱신
                    n_has_2 = 1
                else:
                    n_has_2 = 0
                # 중간 지점을 거친채로 방문하지 않은 곳이니?
                if not visited[nr][nc][pattern_usage][n_has_2]:   
                    # 방문 처리하고 이동하고 deque에 추가
                    visited[nr][nc][pattern_usage][n_has_2] = True
                    q.append((nr, nc, pattern_usage, n_has_2, dist + 1))
        # 패턴이 사용할 수 있다면
        if pattern_usage > 0:
            # 이동할 수 있는 위치를 쭉 돌기
            for tr, tc in pattern_moves:
                
                nr, nc = r + tr, c + tc
                # 범위 벗어났는지 확인, 벽 충돌여부 확인
                if 0<= nr < N and 0 <= nc < M and MAP[nr][nc] != 1:
                    # 중간 지점을 방문한 상태고 현재 중간 지점을 만났다면,
                    if has_2 == 1 or MAP[nr][nc] == 2:
                        # 중간 지점을 거쳤다고 갱신
                        n_has_2 = 1
                    else:
                        n_has_2 = 0
                    # 패턴을 한번 사용했고, 중간 지점을 거쳤다고 갱신한 곳이 아직 방문하지 않은 곳이니?    
                    if not visited[nr][nc][pattern_usage - 1][n_has_2]:
                        # 방문 처리 후, 이동하고 패턴 사용하고 다시 추가
                        visited[nr][nc][pattern_usage - 1][n_has_2] = True
                        q.append((nr, nc, pattern_usage-1, n_has_2, dist + 1))
    # 갈 곳이 없다면 -1 출력
    return -1

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
pattern = [list(map(int, input().split())) for _ in range(5)]

# 패턴에서 이동 가능한 위치 저장 
pattern_moves = []
for i in range(5):
    for j in range(5):
        if pattern[i][j] == 1:
            pattern_moves.append((i - 2, j - 2)) # 3행 3열은 (2 , 2)이므로 위치 갱신
# 방문 여부 계산 (참, 거짓 여부 확인 False * 2), 남은 패턴 수 : 0 ~ K 이므로 K + 1로 정의
# 가로, 세로는 N, M으로 정의
visited = [[[[False] * 2 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, K, 0))