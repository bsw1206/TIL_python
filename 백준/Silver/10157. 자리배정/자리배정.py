import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = int(input())
arr = [[0] * M for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
direction = 0
r, c = 0, 0
cnt = 1
for i in range(N * M):
    arr[r][c] = cnt
    nr = r + dr[direction]
    nc = c + dc[direction]
    cnt += 1
    if not(0<=nr<N and 0<=nc<M) or arr[nr][nc] != 0:
        direction = (direction + 1) % 4
        nr = r + dr[direction]
        nc = c + dc[direction]
        r, c = nr, nc
    else:
        r, c = nr, nc

if num > N * M:
    print(0)
else:        
    for r in range(N):
        for c in range(M):
            if arr[r][c] == num:
                print(r + 1, c + 1)
                break

