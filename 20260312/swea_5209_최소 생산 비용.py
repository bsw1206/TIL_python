import sys
sys.stdin = open('swea_5209_최소 생산 비용.txt')
def dfs(cur_loc, sum_val):

    global min_val

    if sum_val >= min_val:
        return
    
    if cur_loc == N:
        min_val = min(min_val, sum_val)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(cur_loc + 1, sum_val + arr[cur_loc][i])
            visited[i] = False
T = int(input())
for tc in range(1, T  + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_val = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_val}')