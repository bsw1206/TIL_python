import sys
sys.stdin = open('boj_1952_달팽이.txt')
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [[0] * N for _ in range(M)]
arr[0][0] = 1
direction = 0
r, c = 0, 0
cnt = 0
for _ in range(M * N - 1):
    nr, nc = r + dr[direction], c + dc[direction]
    if not (0<= nr < M and 0<= nc < N) or arr[nr][nc]:
        direction = (direction + 1) % 4
        cnt += 1
        nr, nc = r + dr[direction], c + dc[direction]
    arr[nr][nc] = 1
    r, c = nr, nc
print(cnt)