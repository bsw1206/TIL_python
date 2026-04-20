
def dfs(idx, cur_val):
    global min_val

    if cur_val >= min_val:
        return
    if idx == D:
        if check():
            min_val = min(min_val, cur_val)
        return
    
    dfs(idx + 1, cur_val)

    original_row = film[idx][:]

    film[idx] = [0] * W
    dfs(idx + 1, cur_val + 1)
    film[idx] = [1] * W
    dfs(idx + 1, cur_val + 1)
    film[idx] = original_row

def check():
    for c in range(W):
        max_cnt = 1
        cnt = 1
        for r in range(1, D):
            if film[r][c] == film[r-1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                max_cnt = cnt
                break
        if max_cnt < K:
            return False
    return True
    
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    if K == 1:
        print(f'#{tc} 0')
        continue
    min_val = K
    dfs(0, 0)
    print(f'#{tc} {min_val}')
