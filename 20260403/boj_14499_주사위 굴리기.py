# 바닥면이 6, 윗면이 1, 동쪽 면이 3, 서쪽 면이 4, 뒤쪽 면이 2, 앞쪽 면이 5
import sys
sys.stdin = open('boj_14499_주사위 굴리기.txt')

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))


dice = [0, 0, 0, 0, 0, 0]


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


for cmd in order:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    if not(0<=nx< N and 0<= ny < M):
        continue
    one, two, three, four, five, six = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]


    if cmd == 1:
        dice[3], dice[0], dice[2], dice[5] = six, four, one, three
    elif cmd == 2:
        dice[3], dice[0], dice[2], dice[5] = one, three, six, four
    elif cmd == 3:
        dice[0], dice[4], dice[5], dice[1] = five, six, two, one
    elif cmd == 4:
        dice[0], dice[4], dice[5], dice[1] = two, one, five, six 


    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0


    x, y = nx, ny

    print(dice[0])
