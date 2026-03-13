import sys
sys.stdin = open('swea_1486_장훈이의 높은선반.txt')


def dfs(sum_val, cnt):
    global min_val

    if sum_val > min_val:
        return

    if sum_val >= B:
        min_val = min(sum_val, min_val)
        return
    
    if cnt == N:
        return

    dfs(sum_val + S_lst[cnt], cnt + 1)

    dfs(sum_val, cnt + 1)

T = int(input())
for tc in range(1, T + 1): 
    N, B = map(int, input().split())
    S_lst = list(map(int, input().split()))
    min_val = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_val- B}')

###########################################################

from itertools import combinations


T = int(input())
for tc in range(1, T + 1): 
    N, B = map(int, input().split())
    S_lst = list(map(int, input().split()))
    min_val = float('inf')

    for i in range(1, N + 1):
        for j in combinations(S_lst, i):
            
            sum_val = sum(j)

            if sum_val >= B:
                min_val = min(min_val, sum_val - B)
    print(f'#{tc} {min_val}')

            
