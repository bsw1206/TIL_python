dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
import sys
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


            