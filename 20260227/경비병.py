import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                for i in range(4):
                    for j in range(1, N):
                        nr, nc = r + j * dr[i], c + j * dc[i]
                        if 0<= nr< N and 0<= nc < N:
                            if arr[nr][nc] == 1:
                                break  
                            else:
                                arr[nr][nc] = "ang gimothi"
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')
                        

        