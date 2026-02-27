import sys
sys.stdin = open('swea_4615_재미있는 오셀로 게임.txt')
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    c = N // 2
    info_lst = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0] * N for _ in range(N)]
    arr[c][c] = 2
    arr[c-1][c] = 1
    arr[c][c-1] = 1
    arr[c-1][c-1] = 2
    for start_r, start_c, color in info_lst:
        r, c = start_r - 1, start_c - 1
        arr[r][c] = color
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            change_lst = []
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    break
                if arr[nr][nc] == color:
                    for a, b in change_lst:
                        arr[a][b] = color
                    break
                else:
                    change_lst.append((nr, nc))
                    nr += dr[i]
                    nc += dc[i]
    white = 0
    black = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                black += 1
            elif arr[r][c] == 2:
                white += 1
    print(f'#{tc} {black} {white}')
