# N * N 크기의 보드판이 주어졌을 때 
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하기
# 한번의 이동은 전체 블록은 상하좌우 네 방향 중 하나로 이동시킴.
# 같은 값을 갖는 두 블록이 충돌하면 두 블록이 하나로 합쳐지게 된다.
# 다른 값이면 합쳐지지 않는다.
# 위, 아래, 왼쪽, 오른쪽으로 갈 때 정의를 다 해줘야겠네?
# 한 곳으로 붙어야 하니까 왼쪽이나 위쪽은 원래 범위대로 for i in range(N)
# 오른쪽, 아래쪽은 바닥부터 세야 하므로 for i in range(N-1, -1, -1)
# 로직을 짤때 범위만큼 이동하고 0을 만났을 경우에는 계속 이동하고 다른 수를 만나면 전의 이동위치까지로 갱신
# 같은 수를 만나면 arr[r][c] ** 2로 arr[nr][nc] 값을 갱신함.
# 상하좌우로 가는 모든 경우를 생각함.

from itertools import product
import sys
sys.stdin = open('boj_12100_2048(Easy).txt')

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