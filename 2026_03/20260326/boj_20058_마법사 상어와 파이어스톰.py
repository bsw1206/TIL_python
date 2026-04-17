# 파이어스톰을 크기가 2^N * 2^N인 격자로 나누어진 얼음판
# 위치 r, c는 격자의 r행 c열, 인덱스는 얼음의 양, 0이면 얼음이 없는 것이다.
# 단계 L을 결정해야 함. 
# 파이어스톰 : 격자를 2^L * 2^L로 나눔, 모든 부분 격자를 시계 방향으로 90도 회전시킴
# 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. 
# (r,c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)
# 파이어스톰은 총 Q번 시전
# 구하려는 것 : 남아있는 얼음의 합, 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 첫째 줄에 남아있는 얼음의 합을 출력, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수
# 덩어리가 없으면 0 출력


# 일단 부분 격자로 나누는 것을 정의, 격자를 시계방향으로 돌림. 
# 격자를 나누고 돌려서 합치기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
import sys
sys.stdin = open('boj_20058_마법사 상어와 파이어스톰.txt')
from collections import deque

def bfs(start_r, start_c, count):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0<= nr < 2**N and 0<=nc < 2**N) and not visited[nr][nc] and arr[nr][nc]:
                count += 1
                visited[nr][nc] = True
                q.append((nr, nc))
                
    return count
            
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
step = list(map(int, input().split()))
for i in range(Q):
    L = 2 ** step[i]
    for r in range(0, 2**N, L):
        for c in range(0, 2**N, L):
            sub_grid = []
            for x in range(r, r + L):
                sub_grid.append(arr[x][c:c+L])
            rotated_lst = [list(row) for row in zip(*sub_grid[::-1])]
            for x in range(L):
                for y in range(L):
                    arr[r+x][c+y] = rotated_lst[x][y]
    melt_lst = []
    for r in range(2**N):
        for c in range(2**N):
            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nr < 2**N and 0<= nc < 2**N:
                    if arr[nr][nc] == 0:
                        cnt += 1
                else:
                    cnt += 1
            if cnt > 1:
                melt_lst.append((r, c))
    for r, c in melt_lst:
        if arr[r][c] > 0:
            arr[r][c] -= 1
sum_val = 0
for r in range(2**N):
    for c in range(2**N):
        sum_val += arr[r][c]
visited = [[False] * (2**N) for _ in range(2**N)]
print(sum_val)

max_val = 0
for r in range(2**N):
    for c in range(2**N):
        if arr[r][c] and not visited[r][c]:
            result = bfs(r, c, 1)
            if max_val < result:
                max_val = result
print(max_val)


            