import sys
sys.stdin = open('swea_11315_오목 판정.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    # 오목 존재 여부만 파악하기 떄문에 8방향으로 탐색할 필요 x
    # 우, 하, 우하, 좌하만 봐도 됨.
    dr = [1, 0, 1, 1]
    dc = [0, 1, 1, -1]
    
    result = "NO"
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                
                for i in range(4):
                    cnt = 0    
                    for j in range(1, N):
                        nr, nc = r + j * dr[i], c + j * dc[i]
                        if 0<= nr < N and 0<= nc < N and board[nr][nc] == 'o':
                            cnt += 1
                        else:
                            break
										# 자기 자신을 이미 포함했기 때문에 4 이상이어도 오목
                    if cnt >= 4: 
                        result = "YES"
                        break

    print(f'#{tc} {result}')