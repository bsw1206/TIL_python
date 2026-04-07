import sys
sys.stdin = open('swea_22654_차윤이의 RC카.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    
    N = int(input())
    field = [list(map(str, input())) for _ in range(N)]
    Q = int(input())
    command_lst = []
    
    for _ in range(Q):
    
        C, com = input().split()
        command_lst.append(com)
    
    
    start_r, start_c = -1, -1
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start_r, start_c = i, j
                break
        if start_r != -1:
            break
            
    result = []
    for command in command_lst:
        r, c = i, j
        d = 0
        check = 0
        for com in command:
            if com == 'R':
                d = (d + 1) % 4
            elif com == 'L':
                d -= 1
                if d == -1:
                    d = 3
            elif com == 'A':
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if field[nr][nc] != 'T':
                        r, c = nr, nc
        if field[r][c] == 'Y':
                check = 1
                
        result.append(check)
    print(f'#{tc}', *result)