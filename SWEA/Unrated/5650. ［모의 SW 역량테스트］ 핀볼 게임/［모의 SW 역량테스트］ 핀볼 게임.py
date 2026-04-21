dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
info = {
    0 : 0,
    1 : [1, 3, 0, 2],
    2 : [3, 0, 1, 2],
    3 : [2, 0, 3, 1],
    4 : [1, 2, 3, 0],
    5 : [1, 0, 3, 2],
}
opposite = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2,
}

def check(r, c, d):
    sum_val = 0
    start_r, start_c = r, c
    nr, nc = r, c
    while True:
        nr += dr[d]
        nc += dc[d]
        if nr == start_r and nc == start_c:
            return sum_val
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            sum_val += 1
            d = opposite[d]
        else:    
            if arr[nr][nc] > 0:
                if arr[nr][nc] >= 1 and arr[nr][nc] <= 5:
                    sum_val += 1
                    d = info[arr[nr][nc]][d]
                    r, c = nr, nc
                elif arr[nr][nc] >= 6 and arr[nr][nc] <= 10:
                    found = False
                    for row in range(N):
                        for col in range(N):
                            if arr[row][col] == arr[nr][nc] and (row, col) != (nr, nc):
                               nr, nc = row, col
                               found = True
                               break
                        if found:
                            break
            elif arr[nr][nc] == -1:
                return sum_val



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                for i in range(4):
                    result = check(r, c, i)
                    if max_val < result:
                        max_val = result
    print(f'#{tc} {max_val}')
