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