for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    cnt = 0
    for i in range(100):
        if arr[99][i] == 2:
            c , r = i, 99
            break
    while r > 0:
        arr[r][c] = 0
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 100 and 0<= nc < 100 and arr[nr][nc] == 1:
                r, c = nr, nc
    print(f'#{tc} {c}')