from itertools import product

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 0 : 상, 1 : 하, 2: 좌, 3: 우
max_val = 0


for j in product(range(4), repeat=5):
    arr = [row[:] for row in lst]
    j = list(j)
    for d in j:
        merged = [[False] * N for _ in range(N)]
        if d == 0:  # 상(위로 올릴 때)
            for r in range(N):
                for c in range(N):
                    if arr[r][c] != 0:
                        tmp = arr[r][c]
                        arr[r][c] = 0
                        nr = r
                        while nr - 1 >= 0 and arr[nr-1][c] == 0:
                            nr -= 1
                        if nr - 1 >= 0 and arr[nr-1][c] == tmp and not merged[nr -1][c]:
                            arr[nr-1][c] = tmp * 2
                            merged[nr-1][c] = True
                        else:
                            arr[nr][c] = tmp

        elif d == 1:
            for r in range(N - 1, -1, -1):  
                for c in range(N):
                    if arr[r][c] != 0:
                        tmp = arr[r][c]
                        arr[r][c] = 0
                        nr = r
                        while nr + 1 < N and arr[nr + 1][c] == 0:
                            nr += 1
                        if nr + 1 < N and arr[nr+1][c] == tmp and not merged[nr+1][c]:
                            arr[nr+1][c] = tmp * 2
                            merged[nr+1][c] = True
                        else:
                            arr[nr][c] = tmp
        elif d == 2:
            for r in range(N):    
                for c in range(N):
                    if arr[r][c] != 0:
                        tmp = arr[r][c]
                        arr[r][c] = 0
                        nc = c
                        while nc - 1 >= 0 and arr[r][nc-1] == 0:
                            nc -= 1
                        if nc - 1 >= 0 and arr[r][nc - 1] == tmp and not merged[r][nc - 1]:
                            arr[r][nc - 1] = tmp * 2
                            merged[r][nc - 1] = True
                        else:
                            arr[r][nc] = tmp
        elif d == 3:
            for r in range(N):
                for c in range(N - 1, -1, -1):
                    if arr[r][c] != 0:
                        tmp = arr[r][c]
                        arr[r][c] = 0
                        nc = c
                        while nc + 1 < N and arr[r][nc + 1] == 0:
                            nc += 1
                        if nc + 1 < N and arr[r][nc + 1] == tmp and not merged[r][nc + 1]:
                            arr[r][nc + 1] = tmp * 2
                            merged[r][nc + 1] = True
                        else:
                            arr[r][nc] = tmp

    for r in range(N):
        for c in range(N):
            if arr[r][c] > max_val:
                max_val = arr[r][c]

print(max_val)