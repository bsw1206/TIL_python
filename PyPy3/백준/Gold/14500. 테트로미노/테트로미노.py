import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def 볼록할철(r, c):
    sum_lst = []
    if r + 1 < N and c + 2 < M and c + 1 < M:
        sum_lst.append(arr[r][c] + arr[r][c + 1] + arr[r + 1][c + 1] + arr[r][c + 2])
    if c + 1 < M and c + 2 < M and 0 <= r - 1:
        sum_lst.append(arr[r][c] + arr[r][c + 1] + arr[r - 1][c + 1] + arr[r][c + 2])
    if r + 1 < N and r + 2 < N and c + 1 < M:
        sum_lst.append(arr[r][c] + arr[r + 1][c] + arr[r + 1][c + 1] + arr[r + 2][c])
    if r + 1 < N and r + 2 < N and c - 1 >= 0:
        sum_lst.append(arr[r][c] + arr[r + 1][c] + arr[r + 1][c - 1] + arr[r + 2][c])
    return max(sum_lst) if len(sum_lst) > 0 else 0

def tetromino(idx, sum_val, r, c):
    global max_val

    if idx == 4:
        max_val = max(max_val, sum_val)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<= nr < N and 0<= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            tetromino(idx+1, sum_val + arr[nr][nc], nr, nc)
            visited[nr][nc] = False
            
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = 0

for r in range(N):
    for c in range(M):
        tetromino(0, 0, r, c)
        max_val_2 = 볼록할철(r, c)
        if max_val < max_val_2:
            max_val = max_val_2
print(max_val)