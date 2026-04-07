import sys
sys.stdin = open('swea_1873_상호의 배틀필드.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    
    N = int(input())
    command = input()
    for i in range(H):
        for j in range(W):
            if arr[i][j] in '^v<>':
                if arr[i][j] == '^':
                    d = 0
                elif arr[i][j] == 'v':
                    d = 1
                elif arr[i][j] == '<':
                    d = 2
                else:
                    d = 3

                r, c = i, j
                break

    for com in command:
        if com == 'U':
            arr[r][c] = '^'
            d = 0
            if 0 <= r - 1:
                if arr[r-1][c] == '.':
                    
                    arr[r][c], arr[r-1][c] = '.', '^'
                    r -= 1
        elif com == 'D':
            arr[r][c] = 'v'
            d = 1
            if r + 1 < H:
                if arr[r+1][c] == '.':
                    
                    arr[r][c], arr[r+1][c] = '.', 'v'
                    r += 1
        elif com == 'L':
            arr[r][c] = '<'
            d = 2
            if 0 <= c - 1:
                if arr[r][c-1] == '.':
                    
                    arr[r][c], arr[r][c-1] = '.', '<'
                    c -= 1
        elif com == 'R':
            arr[r][c] = '>'
            d = 3
            if c + 1 < W:
                if arr[r][c+1] == '.':
                    
                    arr[r][c], arr[r][c+1] = '.', '>'
                    c += 1
        elif com == 'S':
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] in '*#':
                    if arr[nr][nc] == '*':
                        arr[nr][nc] = '.'
                        break
                    else:
                        break
                nr += dr[d]
                nc += dc[d]
    print(f'#{tc}', end = ' ')
    for row in arr:
        print(''.join(row))