T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_lst = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                r_idx, c_idx = r, c
                while r_idx < N and arr[r_idx][c] != 0:
                    r_idx += 1
                r_cnt = r_idx - r
                while c_idx < N and arr[r][c_idx] != 0:
                    c_idx += 1
                c_cnt = c_idx - c
                for i in range(r, r + r_cnt):
                    for j in range(c, c + c_cnt):
                        arr[i][j] = 0
                result_lst.append([r_cnt, c_cnt])
    result_lst.sort(key = lambda x: (x[0] * x[1], x[0]))
    print(f'#{tc} {len(result_lst)}', end = ' ')
    for x, y in result_lst:
        print(f'{x} {y}', end = ' ')
    print()

