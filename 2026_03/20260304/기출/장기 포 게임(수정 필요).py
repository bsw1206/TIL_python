import sys
sys.stdin = open('장기 포 게임.txt')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(board)
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                start_r, start_c = r, c
                for i in range(4):
                    for j in range(1, N):
                        nr, nc = r + j * dr[i], c + j * dc[i]