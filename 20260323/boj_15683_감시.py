# 사무실은 N * M 크기의 직사각형
# CCTV는 5가지 종류
# 1번 : 한쪽 방향, 2번 : 두 방향(반대로 감시), 3번 : (수직으로 감시), 4번 : 세 방향, 5번 : 네 방향
# 벽은 통과할 수 없음.(사각지대), 벽은 6으로 나타냄.
# 감시 영역은 '#'로 나타냄.
# CCTV끼리는 통과할 수 있음.
# 사각지대의 최소 크기를 구하는 프로그램.

# 세로의 크기 N, 가로의 크기 M이 주어짐.

# 일단 CCTV종류에 따른 감시 범위를 정해야 할거 같은데,
# for문을 하나 돌면서 한번에 확인을 하고,
# CCTV의 방문 여부?
# 배열을 복사하여
import sys
sys.stdin = open('boj_15683_감시.txt')
import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
direction = [
    0,
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [1, 3], [0, 3], [1, 2]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

def dfs(idx, arr):
    global min_val

    if idx == len(CCTV_lst):
        cnt = 0
        for r in range(N):
            for c in range(M):
                if arr[r][c] == 0:
                    cnt += 1
        min_val = min(min_val, cnt)
        return


    row, col, type = CCTV_lst[idx]
    for n in direction[type]:
        temp_arr = copy.deepcopy(arr)
        for i in n:

            nr, nc = row, col
            while True:
                nr += dr[i]
                nc += dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if temp_arr[nr][nc] == 6:
                        break
                    elif temp_arr[nr][nc] == 0:
                        temp_arr[nr][nc] = '#'
                else:
                    break
        dfs(idx + 1, temp_arr)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
CCTV_lst = []
min_val = float('inf')

for r in range(N):
    for c in range(M):
        if 1 <= arr[r][c] <= 5:
            CCTV_lst.append((r, c, arr[r][c]))

dfs(0, arr)


print(min_val)